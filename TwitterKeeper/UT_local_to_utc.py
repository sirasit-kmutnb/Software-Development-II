from Twitter_keeper import PullTweetsData
import unittest
import pytz
from datetime import datetime


class Test_utc_to_local(unittest.TestCase):

    def setUp(self):
        self.puller = PullTweetsData()
        self.localTZ = pytz.timezone('Asia/Bangkok')

    def test_local_to_utc(self):
        # UTC time to convert
        local_dt = datetime(2023, 1, 23, 13, 15, 20)

        # Expected local time
        expected_output = datetime(2023, 1, 23, 6, 15, 20, tzinfo=pytz.UTC)

        # Output from utc_to_local method
        output = self.puller.local_to_utc(local_dt)

        self.assertEqual(expected_output, output)

    def test_local_to_utc_1(self):
        # UTC time to convert
        local_dt = datetime(2023, 1, 1, 6, 0, 0)

        # Expected local time
        expected_output = datetime(2022, 12, 31, 23, 0, 0, tzinfo=pytz.UTC)

        # Output from utc_to_local method
        output = self.puller.local_to_utc(local_dt)

        self.assertEqual(expected_output, output)

    def test_local_to_utc_2(self):
        # UTC time to convert
        local_dt = "2023, 1, 1, 24, 0, 0,"

        # Expected local time
        expected_output = "Bad Data"

        # Output from utc_to_local method
        output = self.puller.local_to_utc(local_dt)

        self.assertEqual(expected_output, output)


if __name__ == '__main__':
    unittest.main()
