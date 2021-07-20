import moveZeros

class Test_MoveZeros_MoveZeroes:
    def test_moveZeroes_1(self):
        result = moveZeros.moveZeroes([0, 1, 0, 3, 12])
        assert result == [1, 3, 12, 0, 0]
