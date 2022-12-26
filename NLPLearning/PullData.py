import tweepy
import pandas as pd

class PullTweetsData():
    def __init__(self):
        self.__count = 0
        
    def getAccessToAPI(self,api_key,api_key_secret):
        self.__auth = tweepy.OAuthHandler(api_key,api_key_secret)

    def setUserAuthentication(self,access_token,access_token_secret):
        self.__auth.set_access_token(access_token,access_token_secret)

    def getTwitterAPI(self):
        self.__api = tweepy.API(self.__auth)

    def createDataFrame(self):
        self.__df = pd.DataFrame(columns=["text","hashtag"])

    def pullTweets(self,query,amount):
        for tweet in tweepy.Cursor(self.__api.search_tweets,q=query,count=100,
            result_type="recent",tweet_mode='extended').items():
            entity_hashtag = tweet.entities.get('hashtags')
            hashtag = ""
            for i in range(0,len(entity_hashtag)):
                hashtag = hashtag +"/"+entity_hashtag[i]["text"]
            try:
                text = tweet.retweeted_status.full_text
            except:
                text = tweet.full_text
            new_data = pd.Series([text,hashtag],index=self.__df.columns)
            self.__df = pd.concat([self.__df,pd.DataFrame(new_data).T],ignore_index=True)
            self.__count += 1
            print(f"Pulled Tweets : {self.__count} tweets")
            if self.__count == amount:
                print("done")
                self.__count = 0
                break

    def saveTweets(self,excelFileName):
        self.__df.to_excel(f"{excelFileName}.xlsx")

api_key = "SnxucIPt1fg7UUyVOT0T5j0pR"
api_key_secret = "yaToQPv95OA1fiNTHD8drKM8g8rZGM7jSQnPOLoxU3QA9UpaLm"
access_token = "1722424471-Xb0DjPVOqXsLj2sXEYXmU2sqxaDC4B793erGO6J"
access_token_secret = "D2LyXN11zAoZB0M476eb1ZGDM55oRvy4tBWNb8pR4CO0h"

puller = PullTweetsData()

puller.getAccessToAPI(api_key,api_key_secret)
puller.setUserAuthentication(access_token,access_token_secret)

puller.getTwitterAPI()
puller.createDataFrame()

puller.pullTweets("ครับ",1000)

puller.saveTweets("positiveTweets_1")