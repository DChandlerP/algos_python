import spiralTraverse

class Test_SpiralTraverse_SpiralTraverse:
    def test_spiralTraverse_1(self):
        result = spiralTraverse.spiralTraverse([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        assert result == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    def test_spiralTraverse_2(self):
        result = spiralTraverse.spiralTraverse([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        assert result == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
