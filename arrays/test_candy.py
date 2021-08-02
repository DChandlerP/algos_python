import candy

class Test_Candy_Candy:
    def test_candy_1(self):
        result = candy.candy([1, 0, 2])
        assert result == 5

    def test_candy_2(self):
        result = candy.candy([1, 2, 2])
        assert result == 4
