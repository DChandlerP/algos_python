import isMonotonic

class Test_IsMonotonic_IsMonotonic:
    def test_isMonotonic_1(self):
        result = isMonotonic.isMonotonic([6, 5, 4, 4])
        assert result == True

    def test_isMonotonic_2(self):
        result = isMonotonic.isMonotonic([5, 15, 20, 10])
        assert result == False
