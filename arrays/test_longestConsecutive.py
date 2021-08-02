import longestConsecutiveSequence

class Test_longestConsecutiveSequence_LongestConsecutiveSequence:
    def test_longestConsecutiveSequence_1(self):
        result = longestConsecutiveSequence.longestConsecutiveSequence([100, 4, 200, 1, 3, 2])
        assert result == 4

    def test_longestConsecutiveSequence_2(self):
        result = longestConsecutiveSequence.longestConsecutiveSequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
        assert result == 9
