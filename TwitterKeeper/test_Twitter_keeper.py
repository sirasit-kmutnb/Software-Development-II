import unittest
from unittest.mock import MagicMock, patch
import tweepy
from datetime import datetime
from Twitter_keeper import PullTweetsData


class TestPullTweetsData(unittest.TestCase):
    def setUp(self):
        self.pull_tweets = PullTweetsData()
        self.api_key = "test_api_key"
        self.api_key_secret = "test_api_key_secret"
        self.access_token = "test_access_token"
        self.access_token_secret = "test_access_token_secret"
        self.pull_tweets.getAccessToAPI(self.api_key, self.api_key_secret)
        self.pull_tweets.setUserAuthentication(
            self.access_token, self.access_token_secret)
        self.pull_tweets.getTwitterAPI()

    def test_getAccessToAPI(self):
        self.assertEqual(
            self.pull_tweets._PullTweetsData__auth.consumer_key, self.api_key)
        self.assertEqual(
            self.pull_tweets._PullTweetsData__auth.consumer_secret, self.api_key_secret)

    def test_setUserAuthentication(self):
        self.assertEqual(
            self.pull_tweets._PullTweetsData__auth.access_token, self.access_token)
        self.assertEqual(
            self.pull_tweets._PullTweetsData__auth.access_token_secret, self.access_token_secret)

    def test_getTwitterAPI(self):
        self.assertIsInstance(
            self.pull_tweets._PullTweetsData__api, tweepy.API)

    def test_getHashtag(self):
        entity_hashtag = [{"text": "test1"}, {"text": "test2"}]
        expected_hashtag = "#test1#test2"
        self.assertEqual(self.pull_tweets.getHashtag(
            entity_hashtag), expected_hashtag)

    def test_createDictData(self):
        tweet_author = "test_author"
        tweet_create_at = datetime.now()
        hashtag = "#test"
        keyword = "test"
        text = "test text"
        location = "test location"
        expected_tweet = {
            "tweet_author": tweet_author,
            "tweet_create_at": tweet_create_at,
            "hashtag": hashtag,
            "keyword": keyword,
            "text": text,
            "tweet_location": location
        }
        self.assertEqual(self.pull_tweets.createDictData(
            tweet_author, tweet_create_at, location, hashtag, keyword, text), expected_tweet)

    def test_pullTweets(self):
        pass  # This method cannot be unit tested as it starts a thread

    # @patch('tweepy.Cursor')
    # def test_pullTweetsThread(self, mock_cursor):
    #     mock_cursor.return_value.items.return_value = [
    #         tweepy.models.Status(
    #             id=1,
    #             entities={'hashtags': [{'text': 'test1'}, {'text': 'test2'}]},
    #             user=tweepy.models.User(screen_name='test_author'),
    #             created_at=datetime.now(),
    #             retweeted_status=None,
    #             full_text='test text'
    #         ) for i in range(5)
    #     ]
    #     self.pull_tweets.pullTweetsThread("test", 5)
    #     self.pull_tweets.getHashtag.assert_called_once()
    #     self.pull_tweets.createDictData.assert_called_once()
    #     self.pull_tweets.saveTweetsDict.assert_called_once()
    #     self.assertEqual(self.pull_tweets._PullTweetsData__count, 0)

    @patch('pymongo.MongoClient')
    def test_connectToDB(self, mock_client):
        pull_tweets_data = PullTweetsData()
        database = 'mydb'
        collection = 'tweets'
        pull_tweets_data.connectToDB(database, collection)
        mock_client.assert_called_with('localhost', 27017)
        mock_client().__getitem__.assert_called_with(database)
        mock_client().__getitem__().__getitem__.assert_called_with(collection)

    @patch('pymongo.MongoClient')
    def test_saveTweetsDict(self, mock_client):
        pull_tweets_data = PullTweetsData()
        mock_db = MagicMock()
        mock_client().__getitem__().__getitem__.return_value = mock_db
        pull_tweets_data.connectToDB('mydb', 'tweets')
        tweet_post = {"tweet_create_at": "2022-01-01",
                      "tweet_author": "John Doe", "text": "Hello World!"}
        pull_tweets_data.saveTweetsDict(tweet_post)

        # check that update_one method is called with correct arguments
        mock_db.update_one.assert_called_with(
            {"tweet_create_at": "2022-01-01", "tweet_author": "John Doe"}, {"$set": tweet_post}, upsert=True)


if __name__ == '__main__':
    unittest.main()
