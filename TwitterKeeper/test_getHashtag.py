from Twitter_keeper import PullTweetsData
import unittest

# def getHashtag(self, entity_hashtag):
#         hashtag = ""
#         for i in range(0, len(entity_hashtag)):
#             hashtag = hashtag + "#"+entity_hashtag[i]["text"]
#         return hashtag

class TestgetHashtag(unittest.TestCase):
    def setUp(self):
        self.twitterKeeper = PullTweetsData()
    
    def test_getHashtag(self):
        entity_hashtag = [
            {"text": "AAA"},
            {"text": "BBB"},
            {"text": "CCC"}
        ]
        expected_output = "#AAA#BBB#CCC"
        self.assertEqual(self.twitterKeeper.getHashtag(entity_hashtag), expected_output)

    def test_getHashtag1(self):
        entity_hashtag = [
            {"text": "AAA"}
        ]
        expected_output = "#AAA"
        self.assertEqual(self.twitterKeeper.getHashtag(entity_hashtag), expected_output)

    def test_getHashtag2(self):
        entity_hashtag = []
        expected_output = ""
        self.assertEqual(self.twitterKeeper.getHashtag(entity_hashtag), expected_output)
    
if __name__ == '__main__':
    unittest.main()