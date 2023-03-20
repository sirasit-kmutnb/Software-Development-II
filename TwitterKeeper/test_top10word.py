from Twitter_Analyzer import FindTopWord
import unittest
from unittest.mock import MagicMock

class TestMostTop10Word(unittest.TestCase):

    def setUp(self) -> None:
        self.anlz = FindTopWord()

    def test_tokenize(self):
        mock_d = "สอบ/ข้อสอบ/A-Level/Eng"
        expected_result = ['สอบ', 'ข้อสอบ', 'A-Level','Eng']
        result = self.anlz.tokenize(mock_d)
        self.assertEqual(result, expected_result)

    def test_prepared_Text(self):
        mock_text_list = [
            {'text': 'เจอโจทย์แล้วเหม่อเลย…🫥🫠'},
            {'text': 'ในที่สุดก็จะได้เล่นเกมเเล้ว😭😭'},
            {'text': 'ไม่ต้องรอ🔥'}
        ]
        mock_preprocessed_text = ['เจอโจทย์แล้วเหม่อเลย', 'ในที่สุดก็จะได้เล่นเกมเเล้ว', 'ไม่ต้องรอ']
        self.anlz.preprocessText = MagicMock(return_value=mock_preprocessed_text)
        result = self.anlz.prepared_Text(mock_text_list)
        self.assertEqual(result, mock_preprocessed_text)


if __name__ == "__main__":
    unittest.main()

