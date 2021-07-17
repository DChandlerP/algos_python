import isValidSubSequence

class Test_IsValidSubSequence_IsValidSubsequence:
    def test_isValidSubsequence_1(self):
        result = isValidSubSequence.isValidSubsequence([0, 1, 2, 3, 4, 5, 6, 7], [1, 3, 5, 7])
        assert result == True

    def test_isValidSubsequence_2(self):
        result = isValidSubSequence.isValidSubsequence([1, 3, 5, 7], [2, 4])
        assert result == False