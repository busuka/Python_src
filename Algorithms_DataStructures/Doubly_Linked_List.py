class DList():


    def __init__(self):
        # クラス変数i. iの値はインスタンス間で共有される.
        DList.i = 0

    def insertKey(self, key):
        DList.i += 1
        self.no = DList.i
        self.key = key
        if DList == 1:
            self.prev = None
        else:
            self.prev = DList.i - 1
        self.next = DList.i + 1


# コンポジションで実装. 連結リストはkeyとprevとnextの要素を持つ.個々の属性を連結リストとしてインスタンス変数にするのではなく,
# それら3つをもつクラスをインスタンス変数とすることでわかりやすくなる.
class DLists():

    def __init__(self):
        self.l = []

    # ここでクラスDListをインスタンス化させている.
    def insert(self, key):
        self.l.append(DList.insertKey(key))

    def printList(self):
        print(self.l)

    def getKey(self):
        return [x.key for x in self.l]

    def deleteKey(self, key):
        pass


if __name__ == '__main__':

    dl = DLists()
    dl.insert(50)
    dl.insert(60)
    dl.insert(70)
    dl.insert(40)
    dl.printList()
    print(dl.getKey())
    dl.deleteKey(50)
