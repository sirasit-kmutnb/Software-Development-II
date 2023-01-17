import unittest
from Twitter_keeper import PullTweetsData

class TestPreprocessingMethods(unittest.TestCase):
    def setUp(self):
        self.preprocessor = PullTweetsData()
    
    def test_removeSpecialChar(self):
        test_cases = [
            ("Hello World!",     "Hello World"),
            ("Hello! World",     "Hello World"),
            ("Hello World[",     "Hello World"),
            ("Hello World]",     "Hello World"),
            ("-Hello World]",    "Hello World"),
            ("@Hello World]",    "Hello World"),
            ("#$?Hello World]",  "Hello World"),
            ('%+"Hello World]"', "Hello World"),
            ("^_^Hello World]",  "Hello World"),
        ]
        for text, expected_output in test_cases:
            self.assertEqual(self.preprocessor.removeSpecialChar(text), expected_output)
    
    def test_removeEmoji(self):
        test_cases = [
            ("Hello World 🌍", "Hello World"),
            ("Hello 😀 World", "Hello  World"),
            ("Hello World 🚀🚀", "Hello World"),
        ]
        for text, expected_output in test_cases:
            self.assertEqual(self.preprocessor.removeEmoji(text), expected_output)

    def test_removeLink(self):
        test_cases = [
            ("Hello World https://www.example.com", "Hello World"),
            ("Hello https://www.example.com World", "Hello  World"),
            ("https://www.example.com Hello World", "Hello World"),
        ]
        for text, expected_output in test_cases:
            self.assertEqual(self.preprocessor.removeLink(text), expected_output)
    
    def test_preprocessText(self):
        test_cases = [
            ("Hello! World🌍 https://www.example.com", "Hello/World"),
            ("Hello 😀 World 🚀🚀https://www.example.com", "Hello/World"),
            ("https://www.example.com Hello World", "Hello/World"),
        ]
        for text, expected_output in test_cases:
            self.assertEqual(self.preprocessor.preprocessText(text), expected_output)

if __name__ == '__main__':
    unittest.main()
