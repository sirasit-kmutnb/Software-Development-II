import unittest
from unittest.mock import patch


class TestListSum(unittest.TestCase):

    string_of_ints = '1 2 3 4 5'

    string_of_ints_2 = '1 1 1 1 1 1 1 1 1 1'

    @patch('builtins.input', side_effect=[5, string_of_ints])
    def test_sum_string_of_ints(self, mock_inputs):
        result = sum()
        self.assertEqual(result, 15)

    @patch('builtins.input', side_effect=[10, string_of_ints_2])
    def test_sum_string_of_ints_2(self, mock_inputs):
        result = sum()
        self.assertEqual(result, 10)


def sum():
    """Asks for the number of integers the user will type and
    the space separated integers."""
    n = input("Type the number of integers: ")
    L = input("Type the integers separated by space: ")
    L = L.split(' ')
    result = 0
    for num in range(n):
        result += int(L[num])
    return result


if __name__ == '__main__':
    unittest.main()
