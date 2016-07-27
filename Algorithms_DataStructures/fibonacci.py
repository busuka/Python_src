import time


# 再帰によるフィボナッチ数列の実装.
def fibonacci_recurion(n):
    if n == 0 or n == 1: return 1
    return fibonacci_recurion(n - 1) + fibonacci_recurion(n - 2)


# メモ化再帰によるフィボナッチ数列の実装
def fibonacci_memo(n):
    if n == 0 or n == 1:
        f[n] = 1
        return

    if f[n] != 0:
        return f[n]

    print(f[n])
    f[n] = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    return f[n]


def fibonacci_dp(n):
    ff[0] = 1
    ff[1] = 1
    i = 2
    while i < n:
        ff[i] = ff[i-1] + ff[i-2]
        i += 1
    return ff[n-1]

if __name__ == "__main__":
    print([fibonacci_recurion(x) for x in range(10)])

    # 普通の再帰
    current = time.time()
    print(fibonacci_recurion(30))
    print("かかった時間(普通の再帰)" + str(time.time() - current) + "秒")

    # メモ化再帰
    # f = [0 for x in range(100)]
    # print(fibonacci_memo(5))

    # 動的計画法
    ff = [0 for x in range(100)]
    current = time.time()
    print(fibonacci_dp(30))
    print(time.time() - current)