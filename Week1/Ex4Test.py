import unittest

class DuplicateTestCase(unittest.TestCase):
    def test_notDuplicate(self):
        result = isDuplicated([1, 3, 2])
        assert result == False

    def test_notDuplicate2(self):
        result = isDuplicated([1,342,34,123,12,312,3,14,23,42])
        assert result == False

    def test_notDuplicate3(self):
        result = isDuplicated([5,67,8,9,7,4,64,45,3,34,6,36,245])
        assert result == False

    def test_notDuplicate4(self):
        result = isDuplicated([6,7,8,9,4,2,45,66,78,98])
        assert result == False

    def test_notDuplicate5(self):
        result = isDuplicated([10,12,23,34,64,65,67,87])
        assert result == False

    def test_Duplicate(self):
        result = isDuplicated([1,2,7,8,2,5,6,4])
        assert result == True
    
    def test_Duplicate2(self):
        result = isDuplicated([23,4,345,56,46,5,67,5,67,5,67,45])
        assert result == True

    def test_Duplicate3(self):
        result = isDuplicated([1,2,2,3,4,5])
        assert result == True

    def test_Duplicate4(self):
        result = isDuplicated([1,2,3,3,4,5])
        assert result == True

    def test_Duplicate5(self):
        result = isDuplicated([1,2,3,4,4,5])
        assert result == True

    def test_noargs(self):
        result = isDuplicated([])
        assert result == "Null"

def isDuplicated(Array):
    if len(Array) == 0:
        return "Null"
    for i in range(len(Array)):
        for j in range(len(Array)):
            if i == j:
                pass
            elif Array[i] == Array[j]:
                return True
    return False

if __name__ == '__main__':
    unittest.main()