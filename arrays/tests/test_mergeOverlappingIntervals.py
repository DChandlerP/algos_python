import mergeOverlappingIntervals

class Test_MergeOverlappingIntervals_MergeOverlappingIntervals:
    def test_mergeOverlappingIntervals_1(self):
        result = mergeOverlappingIntervals.mergeOverlappingIntervals([[1, 3], [2, 6], [8, 10], [15, 18]])
        assert result == [[1, 6], [8, 10], [15, 18]]

    def test_mergeOverlappingIntervals_2(self):
        result = mergeOverlappingIntervals.mergeOverlappingIntervals([[1, 4], [4, 5]])
        assert result == [[1, 5]]
