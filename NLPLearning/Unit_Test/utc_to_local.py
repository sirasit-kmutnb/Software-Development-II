from PullDataV1 import PullTweetsData
import unittest
import pytz
from datetime import datetime


class Test_utc_to_local(unittest.TestCase):

    def setUp(self):
        self.puller = PullTweetsData()
        self.localTZ = pytz.timezone('Asia/Bangkok')

    def test_utc_to_local(self):
        # UTC time to convert
        utc_dt = datetime(2022, 1, 1, 1, 0, 0, tzinfo=pytz.UTC)

        # Expected local time
        expected_output = self.localTZ.localize(
            datetime(2022, 1, 1, 8, 0, 0))

        # Output from utc_to_local method
        output = self.puller.utc_to_local(utc_dt)

        self.assertEqual(expected_output, output)

    def test_utc_to_local_1(self):
        # UTC time to convert
        utc_dt = datetime(2022, 1, 1, 23, 0, 0, tzinfo=pytz.UTC)

        # Expected local time
        expected_output = self.localTZ.localize(
            datetime(2022, 1, 2, 6, 0, 0))

        # Output from utc_to_local method
        output = self.puller.utc_to_local(utc_dt)

        self.assertEqual(expected_output, output)

    def test_utc_to_local_2(self):
        # UTC time to convert
        utc_dt = "2022, 1, 1, 23, 0, 0,"

        # Expected local time
        expected_output = "Bad Data"

        # Output from utc_to_local method
        output = self.puller.utc_to_local(utc_dt)

        self.assertEqual(expected_output, output)


if __name__ == '__main__':
    unittest.main()
