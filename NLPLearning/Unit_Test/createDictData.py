from PullDataV1 import PullTweetsData
import unittest


class TestcreateDictData(unittest.TestCase):

    def init(self):
        self.obj = PullTweetsData()

    def test_createDictData(self):
        tweet_author = 'John Doe'
        tweet_create_at = '2022-01-01 12:00:00'
        hashtag = '#example'
        keyword = 'test'
        text = 'This is a test tweet'

        expected_output = {'tweet_author': 'John Doe',
                           'tweet_create_at': '2022-01-01 12:00:00',
                           'hashtag': '#example',
                           'keyword': 'test',
                           'text': 'This is a test tweet'}

        output = self.obj.createDictData(
            tweet_author, tweet_create_at, hashtag, keyword, text)

        self.assertEqual(expected_output, output)


if __name__ == '__main__':
    unittest.main()
