import time
import sched
from threading import Thread
from threading import Lock
import tweepy
import pandas as pd
from pythainlp.tokenize import word_tokenize
from pythainlp.corpus import thai_stopwords
from sklearn.feature_extraction.text import CountVectorizer
import emoji
import re
import pymongo
from datetime import datetime, timezone
from dateutil import tz
import pytz
from termcolor import colored
from tqdm import tqdm
import os
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()


class PullTweetsData():

    def __init__(self):
        self.localTZ = pytz.timezone('Asia/Bangkok')

    def getAccessToAPI(self, api_key, api_key_secret):
        self.__auth = tweepy.OAuthHandler(api_key, api_key_secret)

    def setUserAuthentication(self, access_token, access_token_secret):
        self.__auth.set_access_token(access_token, access_token_secret)

    def getTwitterAPI(self):
        self.__api = tweepy.API(self.__auth)

    def getHashtag(self, entity_hashtag):
        hashtag = ""
        for i in range(0, len(entity_hashtag)):
            hashtag = hashtag + "#"+entity_hashtag[i]["text"]
        return hashtag

    def local_to_utc(self, local_dt):
        try:
            time = local_dt
            # Localize the datetime object to the local timezone
            local_time = self.localTZ.localize(time)
            # Convert the localized datetime to UTC
            utc_time = local_time.astimezone(pytz.utc)
            # .normalize might be unnecessary
            return utc_time
        except:
            return "Bad Data"

    def utc_to_local(self, utc_dt):
        try:
            local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(self.localTZ)
            # .normalize might be unnecessary
            return self.localTZ.normalize(local_dt)
        except:
            return "Bad Data"

    def createDictData(self, tweet_author, tweet_create_at, tweet_location, hashtag, keyword, text):
        tweet = {}
        tweet["tweet_author"] = tweet_author
        tweet["tweet_create_at"] = tweet_create_at
        tweet["hashtag"] = hashtag
        tweet["keyword"] = keyword
        tweet["text"] = text
        tweet["tweet_location"] = tweet_location
        return tweet

    def pullTweets(self, query, amount):
        thread = Thread(target=self.pullTweetsThread, args=(query, amount))
        thread.start()

    def pullTweetsThread(self, query, amount):
        count = 0
        for tweet in tweepy.Cursor(self.__api.search_tweets, q=query, count=100,
                                   result_type="recent", tweet_mode='extended').items():
            entity_hashtag = tweet.entities.get('hashtags')
            hashtag = self.getHashtag(entity_hashtag)
            tweet_author = tweet.user.screen_name
            keyword = query
            dt_str = str(tweet.created_at)
            format = "%Y-%m-%d %H:%M:%S%z"
            dt_utc = datetime.strptime(dt_str, format)
            local_zone = tz.tzlocal()
            dt_local = dt_utc.astimezone(local_zone)
            tweet_create_at = dt_local
            tweet_location = tweet.user.location
            try:
                text = tweet.retweeted_status.full_text
            except:
                text = tweet.full_text
            tweet_post = self.createDictData(
                tweet_author, tweet_create_at, tweet_location, hashtag, keyword, text)
            # print(tweet_post)
            saveTweet = Thread(target=self.saveTweetsDict,
                               args=(tweet_post,))
            saveTweet.start()
            print(tweet)
            count += 1
            if count == amount:
                count = 0
                break

    def find_multi(self, author="", keyword="", hashtag="", location="", text="", fromtime="", totime=""):

        if not fromtime and not totime:
            query = {"tweet_author": {"$regex": author},
                     "keyword": {"$regex": keyword},
                     "hashtag": {"$regex": hashtag},
                     "tweet_location": {"$regex": location},
                     "text": {"$regex": text}
                     }
        elif not fromtime or not totime:
            return "Missing Time"

        else:
            new_fromtime = self.splittime(fromtime)
            new_totime = self.splittime(totime)
            try:
                utc_fromtime = self.local_to_utc(datetime(
                    new_fromtime[0], new_fromtime[1], new_fromtime[2], new_fromtime[3], new_fromtime[4], new_fromtime[5]))
                utc_totime = self.local_to_utc(datetime(
                    new_totime[0], new_totime[1], new_totime[2], new_totime[3], new_totime[4], new_totime[5]))
            except:
                return "Bad Data"
            query = {"tweet_author": {"$regex": author},
                     "keyword": {"$regex": keyword},
                     "hashtag": {"$regex": hashtag},
                     "tweet_location": {"$regex": location},
                     "text": {"$regex": text},
                     "tweet_create_at": {
                "$gt": utc_fromtime,
                "$lt": utc_totime
            }}
        count = 0

        cursor = self.__db.find(query)
        setTweets = []
        for i in cursor:
            count += 1
            setTweets.append(i)
        return setTweets

    def splittime(self, time):
        timeset = time.split(".")  # split text from dot and send it to list
        timeset = [int(i) for i in timeset]  # change str to integer
        return timeset

    def connectToDB(self, database, collection):
        client = pymongo.MongoClient('localhost', 27017)
        mydb = client[database]
        self.__db = mydb[collection]

    def saveTweetsDict(self, tweet_post):
        self.__db.update_one({"tweet_create_at": tweet_post["tweet_create_at"], "tweet_author": tweet_post["tweet_author"]},
                             {"$set": tweet_post}, upsert=True)

    def removeSpecialChar(self, text):
        return re.sub(r"[\]\[!-@#$?%+:\"\n^_]", "", text).rstrip()

    def removeEmoji(self, text):
        allchars = [str for str in text]
        emoji_list = [c for c in allchars if c in emoji.EMOJI_DATA]
        return ''.join([str for str in allchars if not any(i in str for i in emoji_list)]).rstrip()

    def removeLink(self, text):
        new_text = re.sub(r'https?:\/\/[^\s]+', '', text)
        # text = re.sub(r'https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE).rstrip()
        link_regex = r"(https?:\/\/[-a-zA-Z0-9@:%._\+~#=]+)"
        return re.sub(link_regex, '', new_text).rstrip().lstrip()

    def preprocessText(self, text):
        text = self.removeLink(text)
        text = self.removeEmoji(text)
        text = self.removeSpecialChar(text)
        SplitedSentence = word_tokenize(text, engine="newmm")
        result = [word for word in SplitedSentence if word not in list(
            thai_stopwords()) and " " not in word]
        return "/".join(result).rstrip()

    def tokenize(self, d):
        result = d.split("/")
        result = list(filter(None, result))
        return result

    def prepared_Text(self, text_list):
        new_text = []
        for text in text_list:
            new_text.append(self.preprocessText(text))
        return new_text


def pullTweetsTask():
    api_key = os.getenv('API_KEY')
    api_key_secret = os.getenv('API_KEY_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

    pullerT1 = PullTweetsData()
    pullerT1.getAccessToAPI(api_key, api_key_secret)
    pullerT1.setUserAuthentication(access_token, access_token_secret)
    pullerT1.getTwitterAPI()
    pullerT1.connectToDB("twitter_keeper", "tweets")
    t1 = Thread(target=pullerT1.pullTweets, args=("#tcas66", 1))
    t1.start()

    # A = pullerT1.find_multi("", "", "", "Bangkok", "",
    #                         "2023.2.12.17.0.0", "2023.2.12.17.40.0")
    # print(A)
    # pullerT1.find_multi(location="Bangkok")
    # pullerT1.find_tweets("hashtag", "tcas", "print")
    # TW = pullerT1.find_multi(location="Bangkok", fromtime="2023.2.12.17.0.0",
    #                          totime="2023432423423.2.12.17.40.0")
    # print(TW)
    # pullerT1.find_tweets("text","ยู")


pullTweetsTask()
