import unittest
import tweepy
from unittest.mock import MagicMock
from Twitter_keeper import PullTweetsData
import tweepy

class TestPullTweetsData(unittest.TestCase):

    def setUp(self):
        self.api_key = 'b1AP2ULpybPSA4QJxwNcIkciB'
        self.api_key_secret = 'vUXGZ9ZJ8a0R4YphK9ZHAfwZduAs5v3iCnsxkOuXcZ9edJTqUM'
        self.access_token = '1552621958780530688-rF7v3RU347dHhd00lKnGRExRI1vLB3'
        self.access_token_secret = '2YTPWAIixuKT2LvaizWI8CstmF6ABdZOXYbMDo0DIvVcR'
        self.pull_tweets_obj = PullTweetsData()
        

    def test_get_access_to_api(self):
        self.pull_tweets_obj.getAccessToAPI(self.api_key, self.api_key_secret)
        self.assertIsNotNone(self.pull_tweets_obj._PullTweetsData__auth)

    def test_set_user_authentication(self):
        self.pull_tweets_obj.getAccessToAPI(self.api_key, self.api_key_secret)
        self.pull_tweets_obj.setUserAuthentication(self.access_token, self.access_token_secret)
        self.assertIsNotNone(self.pull_tweets_obj._PullTweetsData__auth.access_token)
        self.assertIsNotNone(self.pull_tweets_obj._PullTweetsData__auth.access_token_secret)


    def test_get_twitter_api(self):
        self.pull_tweets_obj.getAccessToAPI(self.api_key, self.api_key_secret)
        self.pull_tweets_obj.setUserAuthentication(self.access_token, self.access_token_secret)
        self.pull_tweets_obj.getTwitterAPI()
        self.assertIsInstance(self.pull_tweets_obj._PullTweetsData__api, tweepy.API)

    def test_pull_tweets(self):
        A = tweepy.Cursor
        B = PullTweetsData.getHashtag
        tweepy.Cursor = MagicMock()
        PullTweetsData.getHashtag = MagicMock()

        tweepy.Cursor.return_value = {}



    # def test_pull_tweets(self):
    #     query = "test"
    #     amount = 100
    #     self.pull_tweets_obj.getAccessToAPI(self.api_key, self.api_key_secret)
    #     self.pull_tweets_obj.setUserAuthentication(self.access_token, self.access_token_secret)
    #     self.pull_tweets_obj.getTwitterAPI()
    #     tweets = self.pull_tweets_obj.pullTweets(query, amount)
    #     self.assertEqual(len(tweets), amount)

if __name__ == "__main__":
    unittest.main()