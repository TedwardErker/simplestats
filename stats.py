def mean(vals):
    ''' calculate arithmetic mean of list'''
    assert type(vals) is list, "wrong input format"

    if len(vals) == 0 :

        return 0

    else :

        total = sum(vals)
        length = len(vals)
        return total/length


# print(mean([2,4]))

def test_mean():
      assert mean([2,4]) == 3.0

test_mean()

def test_empty_list():
    assert mean([]) == 0.0

test_empty_list()

