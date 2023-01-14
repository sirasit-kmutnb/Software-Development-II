import time
import sched
from threading import Thread
import tweepy
import pandas as pd
from pythainlp.tokenize import word_tokenize
from pythainlp.corpus import thai_stopwords
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

load_dotenv()


class PullTweetsData():

    def __init__(self):
        self.__count = 0
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

    def utc_to_local(self, utc_dt):
        try:
            local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(self.localTZ)
            # .normalize might be unnecessary
            return self.localTZ.normalize(local_dt)
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
        thread = Thread(target=self.pullTweetsThread, args=(query, amount))
        thread.start()

    def pullTweetsThread(self, query, amount):
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
            if self.__count == amount:
                self.__count = 0
                break

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

    def connectToDB(self, database, collection):
        client = pymongo.MongoClient('localhost', 27017)
        mydb = client[database]
        self.__db = mydb[collection]

    def saveTweetsDict(self, tweet_post):
        self.__db.update_one({"tweet_create_at": tweet_post["tweet_create_at"], "tweet_author": tweet_post["tweet_author"]},
                             {"$set": tweet_post}, upsert=True)


def pullTweetsTask():
    api_key = os.getenv('API_KEY')
    api_key_secret = os.getenv('API_KEY_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

    pullerT1 = PullTweetsData()
    pullerT1.getAccessToAPI(api_key, api_key_secret)
    pullerT1.setUserAuthentication(access_token, access_token_secret)
    pullerT1.getTwitterAPI()
    pullerT1.connectToDB("twitter", "tweets")
    t1 = Thread(target=pullerT1.pullTweets, args=("#dek66", 15000))
    t1.start()


pullTweetsTask()
