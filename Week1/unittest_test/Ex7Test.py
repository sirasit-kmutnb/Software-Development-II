import unittest
import unittest.mock

from Ex7 import solveEqFromFile

class TestFunction(unittest.TestCase):
    mock_file_test1 = """16 200 -10
12
70
1
999
50
20
1000
150
300
200
90
900
40
140
130
30
"""
    mock_file_test2 = """10 10 -6
12
8
9
4
6
7
2
16
13
5
"""
    mock_file_test3 = """12 1000 -1000
123
456
239
235
450
676
416
495
674
343
378
535
"""
    def test_solveEq_case1(self):
        with unittest.mock.patch(
            'builtins.open',
            new=unittest.mock.mock_open(read_data=self.mock_file_test1),
            create=True
        ) as file_mock:
            result = solveEqFromFile('/dev/null')
            assert result == (50, 150, 20, 70, 90, 40, 130, 30)

    def test_solveEq_case2(self):
        with unittest.mock.patch(
            'builtins.open',
            new=unittest.mock.mock_open(read_data=self.mock_file_test2),
            create=True
        ) as file_mock:
            result = solveEqFromFile('/dev/null')
            assert result == (2,8,5,7,4,12,16,6)
            
    def test_solveEq_case3(self):
        with unittest.mock.patch(
            'builtins.open',
            new=unittest.mock.mock_open(read_data=self.mock_file_test3),
            create=True
        ) as file_mock:
            result = solveEqFromFile('/dev/null')
            assert result == None

if __name__ == "__main__" :
    unittest.main()