import unittest
import tweepy
from unittest.mock import MagicMock
from Twitter_keeper import PullTweetsData
import tweepy
from datetime import datetime
from dateutil import tz
import pytz

class TestPullTweetsData(unittest.TestCase):

    def setUp(self):
        self.A = tweepy.Cursor
        self.B = PullTweetsData.getHashtag
        tweepy.Cursor = MagicMock()
        PullTweetsData.createDictData = MagicMock()
        PullTweetsData.getHashtag = MagicMock()
        PullTweetsData.getHashtag.return_value = "#hashtag1#hashtag2"
        datetime.strptime = MagicMock()
        mock_dt_utc = MagicMock()
        datetime.strptime.return_value = mock_dt_utc
        tz.tzlocal = MagicMock()
        mock_dt_utc.astimezone.return_value = datetime(2022, 1, 1, 12, 0, 0, tzinfo=pytz.UTC)

    def tearDown(self):
        tweepy.Cursor = self.A
        PullTweetsData.getHashtag = self.B

    def test_pull_tweets(self):
        query = '#hashtag'
        amount = 1
        mock_tweet = MagicMock()
        mock_tweet.user.screen_name = 'test_user'
        mock_tweet.entities.get.return_value = [{'text': 'hashtag1'}, {'text': 'hashtag2'}]
        mock_tweet.created_at = '2022-01-01 12:00:00+00:00'
        mock_tweet.user.location = 'test_location'
        mock_tweet.retweeted_status.full_text = 'test_text'
        mock_tweet.full_text = 'test_text'
        tweepy.Cursor.return_value = [mock_tweet]
        PullTweetsData.pullTweetsThread(query, amount)
        PullTweetsData.createDictData.assert_called_once_with('test_user', datetime(2022, 1, 1, 12, 0, 0, tzinfo=pytz.UTC), 'test_location', )





        



if __name__ == "__main__":
    unittest.main()