import unittest
import tweepy
from PullDataV1 import PullTweetsData

class TestPullTweetsData(unittest.TestCase):

    def setUp(self):
        self.api_key = 'your_api_key'
        self.api_key_secret = 'your_api_key_secret'
        self.access_token = 'your_access_token'
        self.access_token_secret = 'your_access_token_secret'
        self.pull_tweets_obj = PullTweetsData()
        

    def test_get_access_to_api(self):
        self.pull_tweets_obj.getAccessToAPI(self.api_key, self.api_key_secret)
        self.assertIsNotNone(self.pull_tweets_obj.__auth)

    def test_set_user_authentication(self):
        self.pull_tweets_obj.setUserAuthentication(self.access_token, self.access_token_secret)
        self.assertIsNotNone(self.pull_tweets_obj.__auth.access_token)
        self.assertIsNotNone(self.pull_tweets_obj.__auth.access_token_secret)

    def test_get_twitter_api(self):
        self.pull_tweets_obj.getAccessToAPI(self.api_key, self.api_key_secret)
        self.pull_tweets_obj.setUserAuthentication(self.access_token, self.access_token_secret)
        self.pull_tweets_obj.getTwitterAPI()
        self.assertIsInstance(self.pull_tweets_obj.__api, tweepy.API)

if __name__ == "__main__":
    unittest.main()