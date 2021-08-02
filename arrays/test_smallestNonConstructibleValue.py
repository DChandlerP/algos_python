import smallestNonConstructibleValue

class Test_smallestNonConstructibleValue_FindSmallest:
    def test_findSmallest_1(self):
        result = smallestNonConstructibleValue.findSmallest([1, 2, 4])
        assert result == 8

    def test_findSmallest_2(self):
        result = smallestNonConstructibleValue.findSmallest([1, 2, 5])
        assert result == 4
