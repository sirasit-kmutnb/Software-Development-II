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


class Twitter_Keeper:

    def pullTweets(self, query, amount):
        for tweet in tqdm(tweepy.Cursor(self.__api.search_tweets, q=query, count=100,
                                        result_type="recent", tweet_mode='extended').items()):
            entity_hashtag = Thread(
                target=tweet.entities.get, args=('hashtags', ))
            hashtag = Thread(target=self.getHashtag, args=(entity_hashtag))
            tweet_author = Thread(target=tweet.user.screen_name)
            tweet_author =
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
            # print(f"Pulled Tweets : {self.__count} tweets keyword : {query}")
            if self.__count == amount:
                # print(f"Task done with keyword : {query} saved : {self.__count}")
                self.__count = 0
                break
