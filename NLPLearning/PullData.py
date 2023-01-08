import tweepy
import pandas as pd
from pythainlp.tokenize import word_tokenize
from pythainlp.corpus import thai_stopwords
import emoji
import pymongo
from datetime import datetime, timezone
from dateutil import tz
import pytz
from termcolor import colored

import re


class PullTweetsData():
    localTZ = pytz.timezone('Asia/Bangkok')

    def __init__(self):
        self.__count = 0

    def getAccessToAPI(self, api_key, api_key_secret):
        self.__auth = tweepy.OAuthHandler(api_key, api_key_secret)

    def setUserAuthentication(self, access_token, access_token_secret):
        self.__auth.set_access_token(access_token, access_token_secret)

    def getTwitterAPI(self):
        self.__api = tweepy.API(self.__auth)

    def createDataFrame(self):
        self.__df = pd.DataFrame(
            columns=["tweet_create_at", "keyword", "tweet_author", "text", "hashtag"])

    def getHashtag(self, entity_hashtag):
        hashtag = ""
        for i in range(0, len(entity_hashtag)):
            hashtag = hashtag + "#"+entity_hashtag[i]["text"]
        return hashtag

    def utc_to_local(self, utc_dt):
        local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(
            PullTweetsData.localTZ)
        # .normalize might be unnecessary
        return PullTweetsData.localTZ.normalize(local_dt)

    def pullTweets(self, query, amount):
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
            # for i in range(0,len(entity_hashtag)):
            #     hashtag = hashtag +"/"+entity_hashtag[i]["text"]
            try:
                text = tweet.retweeted_status.full_text
            except:
                text = tweet.full_text
            new_data = pd.Series(
                [tweet_create_at, keyword, tweet_author, text, hashtag], index=self.__df.columns)
            self.__df = pd.concat(
                [self.__df, pd.DataFrame(new_data).T], ignore_index=True)
            self.__count += 1
            print(f"Pulled Tweets : {self.__count} tweets")
            if self.__count == amount:
                print("done")
                self.__count = 0
                break

    def removeSpecialChar(self, text):
        return re.sub(r"[!@#$?%+:\"]", "", text)

    def removeEmoji(self, text):
        allchars = [str for str in text]
        emoji_list = [c for c in allchars if c in emoji.EMOJI_DATA]
        return ''.join([str for str in allchars if not any(i in str for i in emoji_list)])

    def removeLink(self, text):
        return re.sub(r'https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)

    def removeEnglish(self, text):
        return re.sub('[^ก-๙]', "", text)

    def connectToDB(self, database, collection):
        client = pymongo.MongoClient('localhost', 27017)
        mydb = client[database]
        self.__db = mydb[collection]

    def saveTweets(self):
        count = 1
        for i in self.__df.to_dict('records'):
            self.__db.update_one({"tweet_create_at": i["tweet_create_at"], "tweet_author": i["tweet_author"]},
                                 {"$set": i}, upsert=True)
            print(f"Saved {count} tweets")
            count += 1

    def preprocessText(self, text):
        text = self.removeEmoji(text)
        text = self.removeSpecialChar(text)
        text = self.removeLink(text)
        text = self.removeEnglish(text)
        SplitedSentence = word_tokenize(text, engine="newmm")
        result = [word for word in SplitedSentence if word not in list(
            thai_stopwords()) and " " not in word]
        return " /".join(result)

    def textSplit(self):
        for i in self.__df["text"].to_list():
            print(self.preprocessText(i))
            print("=============================")

    def find_tweets(self, query, keyword):
        if query == "author":
            q = "tweet_author"
        elif query == "hashtag":
            q = "hashtag"
        for i in self.__db.find({q: keyword}):
            print(colored("======================================", 'red', 'on_red'))
            print(colored("Username : ", 'red',
                  attrs=['bold']), i["tweet_author"])
            print(colored("Create at : ", 'red', attrs=[
                  'bold']), self.utc_to_local(i["tweet_create_at"]))
            print(colored("Text : ", 'cyan', attrs=['bold']), i["text"])
            print(colored("Hashtag : ", 'yellow',
                  attrs=['bold']), i["hashtag"])
            print(colored("======================================", 'red', 'on_red'))

    def splittime(self, time):
        timeset = time.split(".")
        timeset = [int(i) for i in timeset]
        return timeset

    def find_tweets_time(self, fromtime, totime):
        new_fromtime = self.splittime(fromtime)
        new_totime = self.splittime(totime)

        for i in self.__db.find({"tweet_create_at": {
            "$gt": datetime(new_fromtime[0], new_fromtime[1], new_fromtime[2], new_fromtime[3], new_fromtime[4], new_fromtime[5]),
            "$lt": datetime(new_totime[0], new_totime[1], new_totime[2], new_totime[3], new_totime[4], new_totime[5])
        }}):
            print(colored("======================================", 'red', 'on_red'))
            print(colored("Username : ", 'red',
                  attrs=['bold']), i["tweet_author"])
            print(colored("Create at : ", 'red', attrs=[
                  'bold']), self.utc_to_local(i["tweet_create_at"]))
            print(colored("Text : ", 'cyan', attrs=['bold']), i["text"])
            print(colored("Hashtag : ", 'yellow',
                  attrs=['bold']), i["hashtag"])
            print(colored("======================================", 'red', 'on_red'))


api_key = "SnxucIPt1fg7UUyVOT0T5j0pR"
api_key_secret = "yaToQPv95OA1fiNTHD8drKM8g8rZGM7jSQnPOLoxU3QA9UpaLm"
access_token = "1722424471-Xb0DjPVOqXsLj2sXEYXmU2sqxaDC4B793erGO6J"
access_token_secret = "D2LyXN11zAoZB0M476eb1ZGDM55oRvy4tBWNb8pR4CO0h"

puller = PullTweetsData()

puller.getAccessToAPI(api_key, api_key_secret)
puller.setUserAuthentication(access_token, access_token_secret)

puller.getTwitterAPI()
puller.createDataFrame()

# puller.pullTweets("#dek66", 1000)

puller.connectToDB("twitter", "dek66")
# puller.saveTweets()
puller.find_tweets_time("2023.1.8.7.10.0", "2023.1.8.8.0.0")
# puller.find_tweets("author", "thxjeno3")
