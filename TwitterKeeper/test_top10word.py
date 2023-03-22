from Twitter_Analyzer import FindTopWord
import unittest
from unittest.mock import MagicMock
from sklearn.feature_extraction.text import CountVectorizer

class TestMostTop10Word(unittest.TestCase):

    def setUp(self) -> None:
        # self.c = CountVectorizer()
        # CountVectorizer = MagicMock()
        self.anlz = FindTopWord()

    # def tearDown(self) -> None:
    #     CountVectorizer = self.c

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
        self.anlz.preprocessText = MagicMock(return_value="preprocessed_text")
        result = self.anlz.prepared_Text(mock_text_list)
        self.assertEqual(result, ["preprocessed_text","preprocessed_text","preprocessed_text"])

    # def test_Most10WordFinder(self):
        # # Mock the necessary objects
        # CountVectorizer = MagicMock()
        # CountVectorizer.fit_transform.return_value = "transformed_data"
        # CountVectorizer.get_feature_names_out.return_value = ["word1", "word2", "word3"]
        
        # # Call the method with the mocked objects
        # result = self.anlz.Most10WordFinder([{'text':"tweet1"},{'text':"tweet2"}])
        
        # # Check the result
        # self.assertEqual(result.to_dict(), {
        #     'word': ['word1', 'word2', 'word3'],
        #     'count': [1, 1, 1],
        # })
    # def test_most_10_word_finder(self):
    #     # create a mock object for the CountVectorizer
    #     mock_vectorizer = MagicMock()
    #     mock_vectorizer.get_feature_names_out.return_value = ['apple', 'banana','juice', 'fruit']
    #     mock_transformed_data = MagicMock()
    #     mock_transformed_data.sum.return_value = [10, 20, 30, 40]
    #     mock_vectorizer.fit_transform.return_value = mock_transformed_data

    #     # call the method with the mock object
    #     result = self.anlz.Most10WordFinder([{'text':'apple juice'}, {'text':'banana fruit'}])

    #     # assert the result
    #     self.assertEqual(result['word'].tolist(), ['apple','juice', 'banana','fruit'])
    #     self.assertEqual(result['count'].tolist(), [40,30,20,10])

    #     # assert that the mock object was called correctly
    #     mock_vectorizer.fit_transform.assert_called_once_with(self.anlz.prepared_Text(['I love apple juice', 'banana is my favorite fruit']))
    #     mock_vectorizer.get_feature_names_out.assert_called_once()



if __name__ == "__main__":
    unittest.main()

