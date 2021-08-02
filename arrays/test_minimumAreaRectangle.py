import minimumAreaRectangle

class Test_MinimumAreaRectangle_MinimumAreaRectangle:
    def test_minimumAreaRectangle_1(self):
        result = minimumAreaRectangle.minimumAreaRectangle([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]])
        assert result == 4

    def test_minimumAreaRectangle_2(self):
        result = minimumAreaRectangle.minimumAreaRectangle([[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]])
        assert result == 2
