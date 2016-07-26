def ExSearch(list_i, aim):
    """

    aimで指定した値が配列の数字を組み合わせることで算出できればTrueを返す.
    aimから数列の各要素を組み合わせて引いていき、aimが0になれば算出できることを意味する.
    数列の各要素を使用するかしないかの2択なので,再帰を2分割することになる.

    Args:
        list_i: リストの何番目から始めるかを定める変数.初期値 = 0でよい.
        aim:    数列の加算より算出したい数値を決める.

    Returns: True or False

    """
    if aim == 0: return True
    if list_i >= len(testOne): return False
    res0 = ExSearch(list_i + 1, aim)  # 最初の1を引かずに次の数字5へ.(testOne[list_i]を無視している).
    res1 = ExSearch(list_i + 1, aim - testOne[list_i])  # 最初の1を引いて次の数字5へ.
    if res0 == res1 == 0:
        return False
    else:
        return True


def ExSearchDP(i, m):
    if dp[i][m] is not None:
        return dp[i][m]


testOne = [1, 5, 7]
print(ExSearch(0, 12))

dp = [[None for x in range(20)] for y in range(20)]
print(dp)
