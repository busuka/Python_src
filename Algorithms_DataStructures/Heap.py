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




if __name__ == "__main__":
    cbt = CompleteBinaryTree([7, 8, 1, 2, 3])
    cbt.print()
