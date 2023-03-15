import unittest
from Twitter_keeper import PullTweetsData
from mongomock import MongoClient
from datetime import datetime


class TestRemoveTweets(unittest.TestCase):

    def setUp(self):
        self.Puller = PullTweetsData()
        self.mock_client = MongoClient()
        self.mock_db = self.mock_client['test_db']['test_collection']
        self.Puller._PullTweetsData__db = self.mock_db

        self.dummy_tweets = [
            {
                "tweet_author": "anonymous1",
                "tweet_create_at": datetime(2022, 1, 1, 12, 0, 0),
                "hashtag": "#test",
                "keyword": "test",
                "text": "Lorem ipsum dolor sit amet.",
                "tweet_location": "This code"
            },
            {
                "tweet_author": "anonymous2",
                "tweet_create_at": datetime(2022, 1, 1, 12, 12, 0),
                "hashtag": "#test",
                "keyword": "test",
                "text": "Lorem it amet sollicitudin orci.",
                "tweet_location": "This code"
            },
            {
                "tweet_author": "anonymous3",
                "tweet_create_at": datetime(2022, 1, 1, 13, 5, 0),
                "hashtag": "#dummy",
                "keyword": "dummy",
                "text": "Donec egestas mauris laoreet nulla viverra rutrum ac ac metus",
                "tweet_location": "Unknown"
            },
            {
                "tweet_author": "anonymous4",
                "tweet_create_at": datetime(2022, 1, 1, 15, 45, 0),
                "hashtag": "#dummy",
                "keyword": "dummy",
                "text": "Aliquam tincidunt massa vel ante varius pulvinar.",
                "tweet_location": "Unknown"
            }
        ]
        self.mock_db.insert_many(self.dummy_tweets)

    def test_RemoveAuthor(self):
        #test tweet that will remove is exist
        result = self.Puller.find_multi(author="anonymous1")
        self.assertEqual(len(result),1)

        #test that tweet has been removed
        self.Puller.remove_tweet_set(author="anonymous1")
        result = self.Puller.find_multi(author="anonymous1")
        self.assertEqual(len(result),0)

    def test_RemoveHashtag(self):
        #test tweet that will remove is exist
        result = self.Puller.find_multi(hashtag="#test")
        self.assertEqual(len(result),2)

        #test that tweet has been removed
        self.Puller.remove_tweet_set(hashtag="#test")
        result = self.Puller.find_multi(hashtag="#test")
        self.assertEqual(len(result),0)

    def test_RemoveKeyword(self):
        #test tweet that will remove is exist
        result = self.Puller.find_multi(keyword="dummy")
        self.assertEqual(len(result),2)

        #test that tweet has been removed
        self.Puller.remove_tweet_set(keyword="dummy")
        result = self.Puller.find_multi(keyword="dummy")
        self.assertEqual(len(result),0)

    def test_RemoveLocation(self):
        #test tweet that will remove is exist
        result = self.Puller.find_multi(location="Unknown")
        self.assertEqual(len(result),2)

        #test that tweet has been removed
        self.Puller.remove_tweet_set(location="Unknown")
        result = self.Puller.find_multi(location="Unknown")
        self.assertEqual(len(result),0)

    def test_RemoveText(self):
        #test tweet that will remove is exist
        result = self.Puller.find_multi(text="Lorem")
        self.assertEqual(len(result),2)

        #test that tweet has been removed
        self.Puller.remove_tweet_set(text="Lorem")
        result = self.Puller.find_multi(text="Lorem")
        self.assertEqual(len(result),0)

    def test_RemovebyTime(self):
        
        #test tweet that will remove is exist
        result = self.Puller.find_multi(fromtime="2022.1.1.19.10.0", totime="2022.1.1.21.0.0")
        self.assertEqual(len(result),2)

        #test that tweet has been removed
        self.Puller.remove_tweet_set(fromtime="2022.1.1.19.10.0", totime="2022.1.1.21.0.0")
        result = self.Puller.find_multi(fromtime="2022.1.1.19.10.0", totime="2022.1.1.21.0.0")
        self.assertEqual(len(result),0)

        # find tweets that have only fromtime or totime
        result = self.Puller.remove_tweet_set(fromtime="2023.1.1.0.0.0")
        self.assertEqual(result, "Missing Time")

        result = self.Puller.remove_tweet_set(totime="2023.1.1.0.0.0")
        self.assertEqual(result, "Missing Time")

    def test_RemovebyMultiCriteria(self):

        #test tweet that will remove is exist
        result = self.Puller.find_multi(keyword="test", text="Lorem it")
        self.assertEqual(len(result),1)

        #test that tweet has been removed
        self.Puller.remove_tweet_set(keyword="test", text="Lorem it")
        result = self.Puller.find_multi(keyword="test", text="Lorem it")
        self.assertEqual(len(result),0)

        #test tweet that will remove is exist(All Criteria)
        result = self.Puller.find_multi(author="anonymous4", hashtag="#dummy", keyword="dummy",
                                        text="vel", fromtime="2022.1.1.19.10.0", totime="2023.1.1.0.0.0")
        self.assertEqual(len(result),1)

        #test that tweet has been removed
        self.Puller.remove_tweet_set(author="anonymous4", hashtag="#dummy", keyword="dummy",
                                    text="vel", fromtime="2022.1.1.19.10.0", totime="2023.1.1.0.0.0")
        result = self.Puller.find_multi(author="anonymous4", hashtag="#dummy", keyword="dummy",
                                    text="vel", fromtime="2022.1.1.19.10.0", totime="2023.1.1.0.0.0")
        self.assertEqual(len(result),0)

    def test_RemovebyNullCriteria(self):

        #test all tweet that will remove is exist
        result = self.Puller.find_multi()
        self.assertEqual(len(result),4)

        #test that all tweet has been removed
        self.Puller.remove_tweet_set()
        result = self.Puller.find_multi()
        self.assertEqual(len(result),0)


    def test_RemovebyUnexpextedCriteria(self):
        result = self.Puller.remove_tweet_set(
            fromtime="99999.99.99.99.99.99", totime="99999.99.99.99.99.99")
        self.assertEqual(result, "Bad Data")


if __name__ == "__main__":
    unittest.main()
