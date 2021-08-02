import longestMtn

class Test_LongestMtn_LongestMountainInArray:
    def test_longestMountainInArray_1(self):
        result = longestMtn.longestMountainInArray([2, 1, 4, 7, 3, 2, 5])
        assert result == 5

    def test_longestMountainInArray_2(self):
        result = longestMtn.longestMountainInArray([2, 2, 2])
        assert result == 0
