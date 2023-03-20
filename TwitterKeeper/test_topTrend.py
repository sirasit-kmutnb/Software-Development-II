import unittest
from unittest.mock import MagicMock
from Twitter_keeper import PullTweetsData
from Twitter_Analyzer import main

import tweepy

class TestTopTrend(unittest.TestCase):

    def setUp(self):
        tweepy.API = MagicMock()
        MockAPI = MagicMock()
        tweepy.API.return_value = MockAPI
        MockAPI.get_place_trends = MagicMock()
        MockAPI.get_place_trends.return_value = [
            {'trends': [
                {'name': 'Trend 1', 'tweet_volume': 100},
                {'name': 'Trend 2', 'tweet_volume': 200},
                {'name': 'Trend 3', 'tweet_volume': 300},
                {'name': 'Trend 4', 'tweet_volume': 400},
            ]}
        ]

    def test_top_trend(self):
        tweet = PullTweetsData()
        tweet.getTwitterAPI()
        analyzer = main()
        result = analyzer.topTrends()
        expected_output = [{'name': 'Trend 4', 'tweet_volume': 400},
                           {'name': 'Trend 3', 'tweet_volume': 300},
                           {'name': 'Trend 2', 'tweet_volume': 200},
                           {'name': 'Trend 1', 'tweet_volume': 100}]
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()