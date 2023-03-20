from Twitter_keeper import PullTweetsData
import unittest

# def splittime(self, time):
#         timeset = time.split(".")  # split text from dot and send it to list
#         timeset = [int(i) for i in timeset]  # change str to integer
#         return timeset

class TestSplitTime(unittest.TestCase):
    def setUp(self):
        self.twitterKeeper = PullTweetsData()
    
    def test_splittime(self):
        string = "2024.1.1.15.30.0"
        expected_output = [2024, 1, 1, 15, 30, 0]
        self.assertEqual(self.twitterKeeper.splittime(string), expected_output)
    def test_splittime1(self):
        string = "abcdef"
        expected_output = "Bad Input"
        self.assertEqual(self.twitterKeeper.splittime(string), expected_output)
    
if __name__ == '__main__':
    unittest.main()