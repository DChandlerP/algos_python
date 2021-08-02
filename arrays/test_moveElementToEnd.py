import moveElementToEnd

class Test_MoveElementToEnd_MoveZeroes:
    def test_moveZeroes_1(self):
        result = moveElementToEnd.moveZeroes([3, 1, 4, 2], 3)
        assert result == [1, 4, 2, 3]
