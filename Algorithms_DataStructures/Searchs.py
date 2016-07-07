import time
from paiza import ImportCase


def linearSearch(key, list):
    i = 0
    for val in range(len(list)):
        if key == list[i]:
            return i
        i += 1
    return False


def binarySearch(key, list):
    list.sort()
    l = 0
    r = len(list) - 1
    while l < r:
        m = (r + l) // 2
        if key == list[m]:
            return m
        elif key < list[m]:
            r = m
        else:
            l = m
    return False


test_listOne = [10, 8, 4, 19, 2, 20, 5]
test_listTwo = list(map(int, ImportCase.autoinput_returnlist("ALDS1_1Short.txt")))

startt = time.time()
binarySearch(8, test_listTwo)
print(time.time() - startt)
