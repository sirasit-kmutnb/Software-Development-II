# import unittest
# from unittest.mock import patch,Mock
# from Twitter_Analyzer import main

# class TestTwitterAnalyzer(unittest.TestCase):
#     @patch.object(main, 'topTrends', return_value=[
#         {'name': 'trend1'},
#         {'name': 'trend2'},
#         {'name': 'trend3'}
#     ])
#     def test_top10Analyzer(self, mock_topTrends):
#         analyzer = main()
#         analyzer.pull_tweets = Mock()
#         analyzer.tweets_sentiment_analyzer = Mock(return_value=pd.DataFrame({'text': [], 'sentiment': []}))

#         analyzer.top10Analyzer()

#         self.assertEqual(analyzer.pull_tweets.pullTweets.call_count, 3)
#         self.assertEqual(analyzer.tweets_sentiment_analyzer.call_count, 3)