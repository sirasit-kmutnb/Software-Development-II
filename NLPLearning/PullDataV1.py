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
from tqdm import tqdm

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

    def getHashtag(self, entity_hashtag):
        hashtag = ""
        for i in range(0, len(entity_hashtag)):
            hashtag = hashtag + "#"+entity_hashtag[i]["text"]
        return hashtag

    def utc_to_local(self, utc_dt):
        try:
            local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(
                PullTweetsData.localTZ)
            # .normalize might be unnecessary
            return PullTweetsData.localTZ.normalize(local_dt)
        except:
            return "Bad Data"

    def createDictData(self, tweet_author, tweet_create_at, hashtag, keyword, text):
        tweet = {}
        tweet["tweet_author"] = tweet_author
        tweet["tweet_create_at"] = tweet_create_at
        tweet["hashtag"] = hashtag
        tweet["keyword"] = keyword
        tweet["text"] = text
        return tweet

    def pullTweets(self, query, amount):
        for tweet in tqdm(tweepy.Cursor(self.__api.search_tweets, q=query, count=100,
                                        result_type="recent", tweet_mode='extended').items()):
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
            try:
                text = tweet.retweeted_status.full_text
            except:
                text = tweet.full_text
            tweet_post = self.createDictData(
                tweet_author, tweet_create_at, hashtag, keyword, text)
            self.saveTweetsDict(tweet_post)
            self.__count += 1
            # print(f"Pulled Tweets : {self.__count} tweets")
            if self.__count == amount:
                # print("done")
                self.__count = 0
                break

    # def textSplit(self):
    #     for i in self.__df["text"].to_list():
    #         print(self.preprocessText(i))
    #         print("=============================")

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

    # def removeSpecialChar(self, text):
    #     return re.sub(r"[!@#$?%+:\"]", "", text)

    # def removeEmoji(self, text):
    #     allchars = [str for str in text]
    #     emoji_list = [c for c in allchars if c in emoji.EMOJI_DATA]
    #     return ''.join([str for str in allchars if not any(i in str for i in emoji_list)])

    # def removeLink(self, text):
    #     return re.sub(r'https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)

    # def removeEnglish(self, text):
    #     return re.sub('[^ก-๙]', "", text)

    def connectToDB(self, database, collection):
        client = pymongo.MongoClient('localhost', 27017)
        mydb = client[database]
        self.__db = mydb[collection]

    def saveTweetsDict(self, tweet_post):
        self.__db.update_one({"tweet_create_at": tweet_post["tweet_create_at"], "tweet_author": tweet_post["tweet_author"]},
                             {"$set": tweet_post}, upsert=True)

    # def preprocessText(self, text):
    #     text = self.removeEmoji(text)
    #     text = self.removeSpecialChar(text)
    #     text = self.removeLink(text)
    #     text = self.removeEnglish(text)
    #     SplitedSentence = word_tokenize(text, engine="newmm")
    #     result = [word for word in SplitedSentence if word not in list(
    #         thai_stopwords()) and " " not in word]
    #     return " /".join(result)

    # def textSplit(self):
    #     for i in self.__df["text"].to_list():
    #         print(self.preprocessText(i))
    #         print("=============================")



# puller.find_tweets_time("2023.1.8.0.0.0", "2023.1.9.0.0.0")
# puller.find_tweets("hashtag", "#dek66")
# puller.find_tweets("author", "sun_sxe")
from threading import Timer,Thread

def run_every_20_minutes():
    Timer(1 * 60, run_every_20_minutes).start()
    api_key = "b1AP2ULpybPSA4QJxwNcIkciB"
    api_key_secret = "vUXGZ9ZJ8a0R4YphK9ZHAfwZduAs5v3iCnsxkOuXcZ9edJTqUM"
    access_token = "1552621958780530688-rF7v3RU347dHhd00lKnGRExRI1vLB3"
    access_token_secret = "2YTPWAIixuKT2LvaizWI8CstmF6ABdZOXYbMDo0DIvVcR"

    puller = PullTweetsData()

    puller.getAccessToAPI(api_key, api_key_secret)
    puller.setUserAuthentication(access_token, access_token_secret)

    puller.getTwitterAPI()
    puller.connectToDB("twitter", "tweets")
    puller.pullTweets("#dek66", 100)
    t1 = Thread(target=puller.pullTweets, args=("#dek66", 100))
    t2 = Thread(target=puller.pullTweets, args=("#เริ่มต้นปีขอดีบ้างเถาะ", 100))

    t1.start()
    t2.start()

run_every_20_minutes()