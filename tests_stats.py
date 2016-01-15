from stats import mean
from nose.tools import assert_equal, assert_almost_equals


def test_mean():
      assert_equal(mean([2,4]), 3.0)



def test_empty_list():
    assert_equal(mean([]), 0.0)



def test_mean_float():
    assert_equal(mean([3,4]), 3.5)



def test_mean_float2():
    assert_almost_equals(mean([.5,.5,1]), .666666666)

