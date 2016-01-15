from stats import mean


def test_mean():
      assert mean([2,4]) == 3.0

test_mean()

def test_empty_list():
    assert mean([]) == 0.0

test_empty_list()

def test_mean_float():
    assert mean([3,4]) == 3.5

test_mean_float()
