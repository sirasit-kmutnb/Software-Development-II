import unittest


class Sum0TestCase(unittest.TestCase):
    def test_main(self):
        result = Sum0([0, -1, 2, -3, 1, -2])
        assert result == [[-3, 1, 2], [-2, 0, 2], [-1, 0, 1]]

    def test_main1(self):
        result = Sum0([-3, 2, 1])
        assert result == [[-3, 1, 2]]

    def test_main2(self):
        result = Sum0([-5, 2, 3, 9, 7, 1, -2, 0])
        assert result == [[-5, -2, 7], [-5, 2, 3], [-2, 0, 2]]

    def test_main3(self):
        result = Sum0([-1, 0, 1, -1, 2])
        assert result == [[-1, -1, 2], [-1, 0, 1], [-1, 0, 1]]

    def test_false(self):
        result = Sum0([998, 231, 355, 4321, 4314123, 3213123, 45320, 30219, 3210, 9321, 30219])
        assert result == "No Answer"

    def test_main0(self):
        result = Sum0([])
        assert result == "No Answer"


def Sum0(Array):
    Array.sort()
    result = []
    for i in range(len(Array)-2):
        PF, PL = i + 1, len(Array)-1
        while (PF < PL):
            if (Array[i] + Array[PF] + Array[PL] == 0):
                result.append([Array[i], Array[PF], Array[PL]])
                PF += 1
            elif (Array[i] + Array[PF] + Array[PL] > 0):
                PL -= 1
            elif (Array[i] + Array[PF] + Array[PL] < 0):
                PF += 1
    if result == []:
        return "No Answer"
    else:
        return result


if __name__ == '__main__':
    unittest.main()
