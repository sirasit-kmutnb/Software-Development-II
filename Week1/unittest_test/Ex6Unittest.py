import unittest
from unittest.mock import patch


class MixedTenTestCase(unittest.TestCase):

    @patch('builtins.input', side_effect=[1, 4, "1 2 3 4", "1 2 3 4", "1 2 3 4", "1 2 3 4"])
    def test_main(self, mock_inputs):
        result = Mixedten()
        assert result == [4]

    @patch('builtins.input', side_effect=[1, 4, "1 3 5 7", "2 4 8 2", "6 3 1 1", "2 3 5 6"])
    def test_main1(self, mock_inputs):
        result = Mixedten()
        assert result == [7]

    @patch('builtins.input', side_effect=[1, 5, "2 2 2 2 2", "2 2 2 2 2", "2 2 2 2 2", "2 2 2 2 2", "2 2 2 2 2"])
    def test_main2(self, mock_inputs):
        result = Mixedten()
        assert result == [10]

    @patch('builtins.input', side_effect=[1, 4, "1 6 9 8", "1 6 9 8", "1 6 9 8", "1 6 9 8"])
    def test_main3(self, mock_inputs):
        result = Mixedten()
        assert result == [0]

    @patch('builtins.input', side_effect=[2, 4, "1 6 9 8", "1 6 9 8", "1 6 9 8", "1 6 9 8", 5, "2 2 2 2 2", "2 2 2 2 2", "2 2 2 2 2", "2 2 2 2 2", "2 2 2 2 2"])
    def test_main4(self, mock_inputs):
        result = Mixedten()
        assert result == [0, 10]


def Mixedten():
    Result = []
    n = int(input())
    for i in range(n):
        size = int(input())
        Matrix = []
        for i in range(size):
            Matrix.append([int(i) for i in input().split()])
        Result.append(count_row(Matrix)+count_column(Matrix))
    return Result


def count_row(Matrix):
    result = 0
    for i in range(len(Matrix)):
        for start in range(len(Matrix[i])):
            number = 0
            for j in range(len(Matrix[i])-start):
                if number < 10:
                    number += Matrix[i][start+j]
                    if number == 10:
                        result += 1
    return result


def count_column(Matrix):
    result = 0
    for i in range(len(Matrix)):
        for start in range(len(Matrix[i])):
            number = 0
            for j in range(len(Matrix[i])-start):
                if number < 10:
                    number += Matrix[start+j][i]
                    if number == 10:
                        result += 1
    return result


if __name__ == '__main__':
    unittest.main()
