import unittest
from unittest.mock import MagicMock
from Twitter_keeper import PullTweetsData
from mongomock import MongoClient

class TestPullTweetsData(unittest.TestCase):
    def setUp(self):
        self.Puller = PullTweetsData()
        self.mock_client = MongoClient()
        self.mock_db = self.mock_client['test_db']['test_collection']
        self.Puller._PullTweetsData__db = self.mock_db

    def test_save_tweets_dict(self):
        # insert an initial data
        init_tweet = {
            "tweet_create_at": "2022-01-01 12:00:00",
            "tweet_author": "test_author",
            "tweet_text": "test_tweet"
        }

        self.Puller.saveTweetsDict(init_tweet)
        saved_tweet = list(self.mock_db.find({
            "tweet_create_at": "2022-01-01 12:00:00",
            "tweet_author": "test_author"}))

        # Check that saved tweets has one tweet only
        self.assertEqual(len(saved_tweet),1) 
        # Check accuracy between saved tweet and initial tweet
        self.assertEqual(saved_tweet[0]["tweet_create_at"], init_tweet["tweet_create_at"])
        self.assertEqual(saved_tweet[0]["tweet_author"], init_tweet["tweet_author"])
        self.assertEqual(saved_tweet[0]["tweet_text"], init_tweet["tweet_text"])

    def test_overwriting_tweets(self):
        init_tweet = {
            "tweet_create_at": "2022-01-01 12:00:00",
            "tweet_author": "test_author",
            "tweet_text": "test_tweet"
        }
        # insert a duplicate tweets
        self.Puller.saveTweetsDict(init_tweet)
        self.Puller.saveTweetsDict(init_tweet)

        saved_tweet = list(self.mock_db.find({
            "tweet_create_at": "2022-01-01 12:00:00",
            "tweet_author": "test_author"}))

        # Check that saved tweets has unique tweet only
        self.assertEqual(len(saved_tweet),1)
    def test_insert_new_tweets(self):
        init_tweet = {
            "tweet_create_at": "2022-01-01 12:00:00",
            "tweet_author": "test_author",
            "tweet_text": "test_tweet1"
        }
        new_tweet = {
            "tweet_create_at": "2022-01-02 12:00:32",
            "tweet_author": "test_author2",
            "tweet_text": "test_tweet2"
        }
        # insert a duplicate tweets and a new tweet
        self.Puller.saveTweetsDict(init_tweet)
        self.Puller.saveTweetsDict(new_tweet)
        all_tweet = list(self.mock_db.find())

        # Check that saved tweets has unique tweet only
        self.assertEqual(len(all_tweet),2)

        saved_tweet = self.mock_db.find_one({
            "tweet_create_at": "2022-01-02 12:00:32",
            "tweet_author": "test_author2"})

        # Check accuracy between saved tweet and new tweet
        self.assertEqual(saved_tweet["tweet_create_at"], new_tweet["tweet_create_at"])
        self.assertEqual(saved_tweet["tweet_author"], new_tweet["tweet_author"])
        self.assertEqual(saved_tweet["tweet_text"], new_tweet["tweet_text"])

if __name__ == '__main__':
    unittest.main()

