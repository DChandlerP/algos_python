import firstDuplicate

class Test_FirstDuplicate_FirstDuplicate:
    def test_firstDuplicate_1(self):
        result = firstDuplicate.firstDuplicate([10, 5, 3, 4, 3, 5, 6])
        assert result == 3

    def test_firstDuplicate_2(self):
        result = firstDuplicate.firstDuplicate([1, 2, 3])
        assert result == -1

    def test_firstDuplicate_3(self):
        result = firstDuplicate.firstDuplicate([6, 10, 5, 4, 9, 120, 4, 6, 10])
        assert result == 4
