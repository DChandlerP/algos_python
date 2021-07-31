import smallestDifference

class Test_SmallestDifference_SmallestDifference:
    def test_smallestDifference_1(self):
        result = smallestDifference.smallestDifference([1, 3, 11, 15, 2], [23, 127, 235, 19, 8])
        assert result == 3

    def test_smallestDifference_2(self):
        result = smallestDifference.smallestDifference([10, 5, 40], [50, 90, 80])
        assert result == 10
