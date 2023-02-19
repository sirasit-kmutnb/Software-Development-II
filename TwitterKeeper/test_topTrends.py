import unittest
from unittest.mock import patch
from Twitter_Analyzer import main


class TestMain(unittest.TestCase):
    pass
    # @patch('main.PullTweetsData.get_place_trends')
    # def test_top_trends(self, mock_get_trends):
    #     mock_get_trends.return_value = [
    #         {'name': '#Test1', 'url': 'http://twitter.com/search?q=#test1',
    #             'promoted_content': None, 'query': '%test1', 'tweet_volume': 100},
    #         {'name': '#Test2', 'url': 'http://twitter.com/search?q=#test2',
    #             'promoted_content': None, 'query': '%test2',  "tweet_volume": 200},
    #         {'name': '#Test3', 'url': 'http://twitter.com/search?q=#test3',
    #             'promoted_content': None, 'query': '%test3',  "tweet_volume": 300},
    #         {'name': '#Test4', 'url': 'http://twitter.com/search?q=#test4',
    #             'promoted_content': None, 'query': '%test4',  "tweet_volume": None},
    #         {'name': '#Test5', 'url': 'http://twitter.com/search?q=#test5',
    #             'promoted_content': None, 'query': '%test5',  "tweet_volume": 500}
    #     ]
    #     m = main()
    #     trends = m.topTrends()
    #     self.assertEqual(trends, ["#Test3", "#Test5", "#Test2", "#Test1"])
