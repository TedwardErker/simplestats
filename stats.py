def mean(vals):
    ''' calculate arithmetic mean of list'''
    assert type(vals) is list, "wrong input format"
    vals = [float(x) for x in vals]

    if len(vals) == 0 :

        return 0

    else :

        total = sum(vals)
        length = len(vals)
        return total/length

