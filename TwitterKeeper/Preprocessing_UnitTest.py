import unittest
from Twitter_keeper import PullTweetsData



class PreprocessTestCase(unittest.TestCase):
    def setup(self):
        self.puller = PullTweetsData()

    def test_removeEmoji1(self):
        result = self.puller.removeEmoji("😃😄😁😆Hello😅😂🤣🥲")
        assert result == "Hello"

    def test_removeEmoji2(self):
        result = self.puller.removeEmoji("Hello😃😄😁😆😅😂🤣🥲")
        assert result == "Hello"

    def test_removeEmoji3(self):
        result = self.puller.removeEmoji("😃😄😁😆😅😂🤣🥲Hello")
        assert result == "Hello"

    def test_removeSpecialChar1(self):
        result = self.puller.removeSpecialChar("ฮัลโหล!!!!!!!!")
        assert result == "ฮัลโหล"

    def test_removeSpecialChar2(self):
        result = self.puller.removeSpecialChar("ทำไมอ่ะ???")
        assert result == "ทำไมอ่ะ"

    def test_removeSpecialChar3(self):
        result = self.puller.removeSpecialChar("@กรุงเทพ")
        assert result == "กรุงเทพ"

    def test_removeLink1(self):
        result = self.puller.removeLink(
            "สภาพฉันวันคริสต์มาสปีนี้🎄 https://t.co/b2OObKjULZ")
        assert result == "สภาพฉันวันคริสต์มาสปีนี้🎄"


if __name__ == '__main__':
    unittest.main()
