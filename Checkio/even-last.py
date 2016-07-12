def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    if len(array) != 0:
        return sum([val for val in array[0::2]]) * array[len(array)-1]
    else:
        return 0


def checkioNo1(array):
    """
    The simple slice and comprehension.
    """
    return sum(el for el in array[::2]) * array[-1] if array else 0


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
