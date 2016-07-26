import math
def checkio(a, b, c):

    # 辺の長さから角度を求めるためには逆三角関数を用いる.
    # また三角形が成立する条件はある2辺の和がもう1辺の長さより長いことである.
    # asinやacosで戻る値はラジアン.つまり * 180 / math.pi をすればよい.

    if not(a + b > c and b + c > a and a + c > b):
        return [0, 0, 0]
    else:
        math.atan(a/b) * 180 / math.pi  # 37
        math.asin(b/c) * 180 / math.pi  # 53



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
