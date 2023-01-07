from PullData import PullTweetsData
import unittest

class PreprocessTestCase(unittest.TestCase):
    def test_removeEmoji1(self):
        test = PullTweetsData()
        result = test.removeEmoji("😃😄😁😆Hello😅😂🤣🥲")
        assert result == "Hello"

    def test_removeEmoji2(self):
        test = PullTweetsData()
        result = test.removeEmoji("Hello😃😄😁😆😅😂🤣🥲")
        assert result == "Hello"

    def test_removeEmoji3(self):
        test = PullTweetsData()
        result = test.removeEmoji("😃😄😁😆😅😂🤣🥲Hello")
        assert result == "Hello"

    def test_removeSpecialChar1(self):
        test = PullTweetsData()
        result = test.removeSpecialChar("ฮัลโหล!!!!!!!!")
        assert result == "ฮัลโหล"

    def test_removeSpecialChar2(self):
        test = PullTweetsData()
        result = test.removeSpecialChar("ทำไมอ่ะ???")
        assert result == "ทำไมอ่ะ"

    def test_removeSpecialChar3(self):
        test = PullTweetsData()
        result = test.removeSpecialChar("@กรุงเทพ")
        assert result == "กรุงเทพ"

    # def test_preprocessText(self):
    #     test = PullTweetsData()
    #     result = test.preprocessText()


if __name__ == "__main__":
    unittest.main()