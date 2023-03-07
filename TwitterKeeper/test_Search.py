import unittest
from Twitter_keeper import PullTweetsData
from mongomock import MongoClient
from datetime import datetime


class TestFindTweets(unittest.TestCase):

    def setUp(self):
        self.Puller = PullTweetsData()
        self.mock_client = MongoClient()
        self.mock_db = self.mock_client['test_db']['test_collection']
        self.Puller._PullTweetsData__db = self.mock_db

        self.dummy_tweets = [
            {
                "tweet_author": "anonymous",
                "tweet_create_at": datetime(2022, 1, 1, 12, 0, 0),
                "hashtag": "#test",
                "keyword": "test",
                "text": "Lorem ipsum dolor sit amet.",
                "tweet_location": "This code"
            },
            {
                "tweet_author": "anonymust",
                "tweet_create_at": datetime(2022, 1, 1, 12, 12, 0),
                "hashtag": "#test",
                "keyword": "test",
                "text": "Lorem it amet sollicitudin orci.",
                "tweet_location": "This code"
            },
            {
                "tweet_author": "anonymusk",
                "tweet_create_at": datetime(2022, 1, 1, 13, 5, 0),
                "hashtag": "#dummy",
                "keyword": "dummy",
                "text": "Donec egestas mauris laoreet nulla viverra rutrum ac ac metus",
                "tweet_location": "Unknown"
            },
            {
                "tweet_author": "anonymud",
                "tweet_create_at": datetime(2022, 1, 1, 15, 45, 0),
                "hashtag": "#dummy",
                "keyword": "dummy",
                "text": "Aliquam tincidunt massa vel ante varius pulvinar.",
                "tweet_location": "Unknown"
            }
        ]
        self.mock_db.insert_many(self.dummy_tweets)

    def test_FindAuthor(self):
        result = self.Puller.find_multi(author="anonymusk")
        self.assertEqual(result, [self.dummy_tweets[2]])

    def test_FindHashtag(self):
        # find hashtag test
        result = self.Puller.find_multi(hashtag="#test")
        self.assertEqual(result, self.dummy_tweets[0:2])

        # find hashtag dummy
        result = self.Puller.find_multi(hashtag="#dummy")
        self.assertEqual(result, self.dummy_tweets[2:])

    def test_FindKeyword(self):
        # find keyword test
        result = self.Puller.find_multi(keyword="test")
        self.assertEqual(result, self.dummy_tweets[0:2])

        # find keyword dummy
        result = self.Puller.find_multi(keyword="dummy")
        self.assertEqual(result, self.dummy_tweets[2:])

    def test_FindLocation(self):
        # find location This code
        result = self.Puller.find_multi(location="This code")
        self.assertEqual(result, self.dummy_tweets[0:2])

        # find location Unknown
        result = self.Puller.find_multi(location="Unknown")
        self.assertEqual(result, self.dummy_tweets[2:])

    def test_FindText(self):
        # find tweets that has "Lorem" in text
        result = self.Puller.find_multi(text="Lorem")
        self.assertEqual(result, self.dummy_tweets[0:2])

        # find tweets that has "Donec" in text
        result = self.Puller.find_multi(text="Donec")
        self.assertEqual(result, [self.dummy_tweets[2]])

        # find tweets that has "vel" in text
        result = self.Puller.find_multi(text="vel")
        self.assertEqual(result, [self.dummy_tweets[3]])

    def test_FindbyTime(self):
        # find tweets that tweeted in 12:10(19:10 in local) to 14:00(21:00 in local)
        result = self.Puller.find_multi(
            fromtime="2022.1.1.19.10.0", totime="2022.1.1.21.0.0")
        self.assertEqual(result, self.dummy_tweets[1:3])

        # find tweets that tweeted in 2023
        result = self.Puller.find_multi(
            fromtime="2023.1.1.0.0.0", totime="2023.1.2.0.0.0")
        self.assertEqual(result, [])

        # find tweets that have only fromtime or totime
        result = self.Puller.find_multi(fromtime="2023.1.1.0.0.0")
        self.assertEqual(result, "Missing Time")

        result = self.Puller.find_multi(totime="2023.1.1.0.0.0")
        self.assertEqual(result, "Missing Time")

    def test_FindbyMultiCriteria(self):
        # find tweets by keyword and text
        result = self.Puller.find_multi(keyword="test", text="Lorem it")
        self.assertEqual(result, [self.dummy_tweets[1]])

        # find tweets by keyword, text and author
        result = self.Puller.find_multi(
            author="anonymusk", keyword="dummy", text="Donec")
        self.assertEqual(result, [self.dummy_tweets[2]])

        # find tweets by All Criteria
        result = self.Puller.find_multi(author="anonymud", hashtag="#dummy", keyword="dummy",
                                        text="vel", fromtime="2022.1.1.19.10.0", totime="2023.1.1.0.0.0")
        self.assertEqual(result, [self.dummy_tweets[3]])

    def test_FindbyNullCriteria(self):
        # find tweets by null criteria
        result = self.Puller.find_multi()
        self.assertEqual(result, self.dummy_tweets)

    def test_FindbyUnexpextedCriteria(self):
        result = self.Puller.find_multi(
            fromtime="99999.99.99.99.99.99", totime="99999.99.99.99.99.99")
        self.assertEqual(result, "Bad Data")


if __name__ == "__main__":
    unittest.main()
