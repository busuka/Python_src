# 完全二分木では親や左右の子を一発で求めることができる.二分探索木のように大小関係を考える必要もない.
# 実装においてインデックスが1からにしたほうがよいため、注意する.


class CompleteBinaryTree():
    def __init__(self, l):
        self.l = l
        self.len = len(l)
        self.id = [x + 1 for x in range(self.len)]
        self.heap = dict(zip(self.id, self.l))

    def parent(self, i):
        return i // 2

    def left(self, i):
        return i * 2

    def right(self, i):
        return i * 2 + 1

    def print(self):

        for i in range(1, self.len + 1):

            print("NodeID:" + str(i), end=" ")
            print("Key: " + str(self.heap[i]), end=" ")

            if self.parent(i) >= 1: print("Parent : " + str(self.heap[self.parent(i)]), end=" ")
            if self.left(i) <= self.len:  print("Left : " + str(self.heap[self.left(i)]), end=" ")
            if self.right(i) <= self.len: print("Right : " + str(self.heap[self.right(i)]), end=" ")
            print("")


def build_max_heap(l):
    i = len(l) // 2
    while i >= 0:
        max_heap(l, i)
        i -= 1
        print(l)
    return l


def max_heap(l,i):
    left = i * 2
    right = i * 2 + 1

    # 左の子が最大であれば選ぶ.
    if left < len(l) and l[left] > l[i]:
        largest = left

    # 自身が最大もしくは右の子が最大の場合.
    else:
        largest = i

    # 右の子が最大であれば選ぶ.
    if right < len(l) and l[right] > l[i]:
        largest = right

    if i != largest:
        l[i], l[largest] = l[largest], l[i]
        max_heap(l,largest)


if __name__ == "__main__":
    cbt = CompleteBinaryTree([7, 8, 1, 2, 3])
    cbt.print()

    print(build_max_heap([4,1,3,2,16,9,10,14,8,7]))
