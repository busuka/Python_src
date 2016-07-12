import itertools


def checkio1(number):
    v = list(str(number))
    mv = list(map(lambda x: x.replace('0', '1'), v))  # => ['1','2','3','4','1','5']
    nv = list(map(int, mv))
    pdt = 1
    for i in nv:
        pdt = pdt * i
    return pdt


def checkio(number):
    number_list = [x for x in map(int, list(str(number))) if x != 0]  # => [1,2,3,4,5]
    return list(itertools.accumulate(number_list, lambda x, y: x * y))[-1]


def checkioNO1(number):
    res = 1
    for d in str(number):
        res *= int(d) if int(d) else 1  # d = 0 のときはbool値がFalseとなる. Pythonは0が偽.
    return res


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
