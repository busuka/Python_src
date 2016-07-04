def checkio(number):
    v = list(str(number))
    mv = list(map(lambda x: x.replace('0','1'),v))
    nv = list(map(int, mv))
    pdt = 1
    for i in nv:
        pdt = pdt * i
    return pdt


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
