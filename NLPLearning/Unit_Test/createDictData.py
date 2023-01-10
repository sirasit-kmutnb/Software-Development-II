from PullDataV1 import PullTweetsData
import unittest


class TestcreateDictData(unittest.TestCase):

    def setUp(self):
        self.puller = PullTweetsData()

    def test_createDictData(self):
        tweet_author = 'Test Test'
        tweet_create_at = 'times'
        hashtag = '#example'
        keyword = 'test'
        text = 'This is a test tweet'

        expected_output = {'tweet_author': 'Test Test',
                           'tweet_create_at': 'times',
                           'hashtag': '#example',
                           'keyword': 'test',
                           'text': 'This is a test tweet'}

        output = self.puller.createDictData(
            tweet_author, tweet_create_at, hashtag, keyword, text)

        self.assertEqual(expected_output, output)

    def test_createDictData(self):
        tweet_author = ''
        tweet_create_at = ''
        hashtag = ''
        keyword = ''
        text = ''

        expected_output = {'tweet_author': '',
                           'tweet_create_at': '',
                           'hashtag': '',
                           'keyword': '',
                           'text': ''}

        output = self.puller.createDictData(
            tweet_author, tweet_create_at, hashtag, keyword, text)

        self.assertEqual(expected_output, output)


if __name__ == '__main__':
    unittest.main()
