import maxPoints

class Test_MaxPoints_MaxPoints:
    def test_maxPoints_1(self):
        result = maxPoints.maxPoints([[1, 1], [2, 2], [3, 3]])
        assert result == 3
