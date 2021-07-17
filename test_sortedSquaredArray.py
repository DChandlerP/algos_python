import sortedSquaredArray

class Test_SortedSquaredArray_SortedSquaredArray:
    def test_sortedSquaredArray_1(self):
        result = sortedSquaredArray.sortedSquaredArray([-2, 0, 3, 9])
        assert result == [0, 4, 9, 81]

    def test_sortedSquaredArray_2(self):
        result = sortedSquaredArray.sortedSquaredArray([1, 2, 3, 5, 6, 8, 9])
        assert result == [1, 4, 9, 25, 36, 64, 81]
