import unittest
from PullData import PullTweetsData


class PreprocessTestCase(unittest.TestCase):
    def test_removeEng1(self):
        puller = PullTweetsData()
        result = puller.removeEnglish("Helloสวัสดี")
        assert result == "สวัสดี"

    def test_removeEng2(self):
        puller = PullTweetsData()
        result = puller.removeEnglish("สวัสดีครับผมชื่อ Joe มาจาก America")
        assert result == "สวัสดีครับผมชื่อมาจาก"

    def test_removeEng3(self):
        puller = PullTweetsData()
        result = puller.removeEnglish(
            "Maybe พวกเราควรที่จะ Do Something ที่มีประโยชน์นะ555")
        assert result == "พวกเราควรที่จะที่มีประโยชน์นะ"

    def test_removeLink1(self):
        puller = PullTweetsData()
        result = puller.removeLink(
            "สภาพฉันวันคริสต์มาสปีนี้🎄 https://t.co/b2OObKjULZ")
        assert result == "สภาพฉันวันคริสต์มาสปีนี้🎄 "


if __name__ == '__main__':
    unittest.main()
