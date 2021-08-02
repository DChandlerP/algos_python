import fourNumSum
from itertools import chain

class Test_FourNumSum_FourNumberSum:
    def test_fourNumberSum_1(self):
        result = fourNumSum.fourNumberSum([1,0,-1,0,-2,2], 0)
        assert len(result) == 3
        assert set(chain.from_iterable(result)) == set(chain.from_iterable([[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]))
