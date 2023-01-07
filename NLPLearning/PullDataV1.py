import tweepy
import pandas as pd
from pythainlp.tokenize import word_tokenize
from pythainlp.corpus import thai_stopwords
import emoji
import pymongo
from datetime import datetime, timezone
from dateutil import tz
import pytz

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
        self.__db.insert_many(self.__df.to_dict('records'))

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


api_key = "b1AP2ULpybPSA4QJxwNcIkciB"
api_key_secret = "vUXGZ9ZJ8a0R4YphK9ZHAfwZduAs5v3iCnsxkOuXcZ9edJTqUM"
access_token = "1552621958780530688-rF7v3RU347dHhd00lKnGRExRI1vLB3"
access_token_secret = "2YTPWAIixuKT2LvaizWI8CstmF6ABdZOXYbMDo0DIvVcR"

puller = PullTweetsData()

puller.getAccessToAPI(api_key, api_key_secret)
puller.setUserAuthentication(access_token, access_token_secret)

puller.getTwitterAPI()
puller.createDataFrame()

puller.pullTweets("花譜", 10)

puller.connectToDB("twitter", "tweets")
puller.saveTweets()
