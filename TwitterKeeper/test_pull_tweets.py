import unittest
from unittest.mock import MagicMock
from Twitter_keeper import PullTweetsData
import tweepy
import threading

class TestPullTweetsData(unittest.TestCase):

    def setUp(self):
        self.A = tweepy.Cursor
        self.B = PullTweetsData.getHashtag
        tweepy.Cursor = MagicMock()
        self.MockItems = MagicMock()
        tweepy.Cursor.return_value = self.MockItems
        PullTweetsData.createDictData = MagicMock()
        PullTweetsData.getHashtag = MagicMock()
        PullTweetsData.getHashtag.return_value = "#hashtag1#hashtag2"
        threading.Thread = MagicMock()
        PullTweetsData.saveTweetsDict = MagicMock()
        tweepy.API = MagicMock()


    def tearDown(self):
        tweepy.Cursor = self.A
        PullTweetsData.getHashtag = self.B

    def test_pull_tweets(self):
        tweet = PullTweetsData()
        query = '#hashtag'
        amount = 1
        mock_tweet = MagicMock()
        mock_tweet.user.screen_name = 'test_user'
        mock_tweet.entities.get.return_value = [{'text': 'hashtag1'}, {'text': 'hashtag2'}]
        mock_tweet.created_at = '2022-01-01 12:00:00+00:00'
        mock_tweet.user.location = 'test_location'
        mock_tweet.retweeted_status.full_text = 'test_text'
        mock_tweet.full_text = 'test_text'
        self.MockItems.items.return_value = [mock_tweet]
        # tweepy.Cursor.return_value = [mock_tweet]
        tweet.getTwitterAPI()
        tweet.pullTweetsThread(query, amount)
        PullTweetsData.getHashtag.assert_called_once()
        PullTweetsData.createDictData.assert_called_once_with('test_user', '2022-01-01 12:00:00+00:00', 'test_location', "#hashtag1#hashtag2", "#hashtag", "test_text")
        PullTweetsData.saveTweetsDict.assert_called_once()

if __name__ == "__main__":
    unittest.main()