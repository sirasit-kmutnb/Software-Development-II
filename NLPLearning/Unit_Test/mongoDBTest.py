import unittest
from unittest.mock import patch, MagicMock
import pymongo
from PullDataV1 import PullTweetsData

class TestPullTweetsData(unittest.TestCase):
    
    def test_connectToDB(self):
        # Test if the method can select the correct database and collection
        pull_tweets_data = PullTweetsData()
        pull_tweets_data.connectToDB("twitter", "tweets")
        client = pymongo.MongoClient('localhost', 27017)
        self.assertEqual(client['twitter']['tweets'], pull_tweets_data._PullTweetsData__db)

        # database = 'mydb'
        # collection = 'tweets'
        # mock_client.assert_called_with('localhost', 27017)
        # mock_client().__getitem__.assert_called_with(database)
        # mock_client().__getitem__().__getitem__.assert_called_with(collection)

    @patch('pymongo.MongoClient')
    def test_saveTweetsDict(self, mock_client):
        pull_tweets_data = PullTweetsData()
        mock_db = MagicMock()
        mock_client().__getitem__().__getitem__.return_value = mock_db
        pull_tweets_data.connectToDB('mydb', 'tweets')
        tweet_post = {"tweet_create_at": "2022-01-01", "tweet_author": "John Doe", "text": "Hello World!"}
        pull_tweets_data.saveTweetsDict(tweet_post)

        # check that update_one method is called with correct arguments
        mock_db.update_one.assert_called_with({"tweet_create_at": "2022-01-01",
         "tweet_author": "John Doe"}, {"$set": tweet_post}, upsert=True)
  
if __name__ == '__main__':
    unittest.main()