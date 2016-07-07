def factorial(value):
    if value == 1: return 1
    return value * factorial(value - 1)


def findMax(vec, min, max):
    m = (max - min) // 2
    if min == max - 1: return vec[min]

    u = findMax(vec, min, m)
    v = findMax(vec, m, max)
    return max([u,v])



# 階上を求める関数
print(factorial(5))

# 最大値を分割統治法で解く
vector = [1, 31, 25, 56, 56, 8, 4, 3, 81]
findMax(vector, 0, len(vector) - 1)
