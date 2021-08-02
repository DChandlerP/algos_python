import productArray

class Test_ProductArray_ProductArray:
    def test_productArray_1(self):
        result = productArray.productArray([10, 3, 5, 6, 2])
        assert result == [180, 600, 360, 300, 900 ]
