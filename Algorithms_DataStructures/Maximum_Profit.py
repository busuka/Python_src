import time
from paiza import ImportCase


def output_max_One(test_list):
    """
    Alg:
        ひたすら比較を繰り返して最大値を出力する.

    Args:
        test_list: テストしたいリスト

    Returns:
        最大値（答え)

    計算量:
        O(n^2)

    """

    numLoop = test_list[0]
    start_i = 1
    end_i = numLoop + 1
    max_list = []
    for i in range(numLoop - 1):
        cval = test_list[start_i]
        max_list.append(max([x - cval for x in test_list[(start_i + 1):end_i]]))
        start_i += 1

    print(max(max_list))


def output_max_Two(test_list):
    """

    Alg:
        全検索をするのではなく、
        比較する値(Rj)における最小値(Ri)[i < j]を保存してくことで
        O(n)で処理を終了させる.

    Args:
        テストしたいリスト:

    Returns:
        最大値

    """

    minv = test_list[1]
    maxv = -10000000000
    for x in test_list[2:]:
        tmp_max = x - minv
        if tmp_max > maxv:
            maxv = tmp_max
        if x < minv:
            minv = x
    print(maxv)


testOne = [6, 5, 3, 1, 3, 4, 3]
testTwo = [3, 4, 3, 2]
testThree = [7, 3, 2, 4, 1, 5, 3, 6]
testFour = [2, 100000, 1]
testFive = list(map(int, ImportCase.autoinput_returnlist("ALDS1_1Short.txt")))

# Algorithms1での実行 O(n^2)
start_time = time.time()
output_max_One(testOne)
output_max_One(testTwo)
output_max_One(testThree)
output_max_One(testFour)
output_max_One(testFive)
print(time.time() - start_time)

# Algorithm2での実行 O(n)
start_time = time.time()
output_max_Two(testOne)
output_max_Two(testTwo)
output_max_Two(testThree)
output_max_Two(testFour)
output_max_Two(testFive)
print(time.time() - start_time)

'''
提出用コード

def output_max(test_list):
    numLoop = test_list[0]
    start_i = 1
    end_i = numLoop + 1
    max_list = []
    for i in range(numLoop - 1):
        cval = test_list[start_i]
        max_list.append(max([x - cval for x in test_list[(start_i+1):end_i]]))
        start_i += 1

    print(max(max_list))

test_list = []
test_list.append(int(input()))
for x in range(test_list[0]):
    test_list.append(int(input()))
output_max(test_list)
'''

'''
提出用コード

def output_max_Two(test_list):
    minv = test_list[1]
    maxv = -1000000000
    for x in test_list[2:]:
        tmp_max = x - minv
        if tmp_max > maxv:
            maxv = tmp_max
        if x < minv:
            minv = x
    print(maxv)

test_list = []
test_list.append(int(input()))
for x in range(test_list[0]):
    test_list.append(int(input()))
output_max_Two(test_list)
'''
