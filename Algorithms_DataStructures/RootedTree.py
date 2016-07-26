import pprint
import copy as cp


# 8.2 根付き木の表現
class RootedTree():
    # Rooted Treeでは,Left = 左の子, Right = すぐ右の兄弟とする.
    # Rooted Treeは子を3つ以上持つこともあるため、LeftとRightでは表現できない.
    # 子を２つしか持たないBinary Treeでは,Left = 左の子,    Right = 右の子となる.

    def __init__(self):
        self.nodes = []
        self.parents = []
        self.lefts = []
        self.rights = []
        self.depthTable = []
        self.tmpTable = []

    def insert(self, nodeid, parent=None, left=None, right=None):
        self.nodes.append(nodeid)
        self.parents.append(parent)
        self.lefts.append(left)
        self.rights.append(right)
        self.depthTable.append(None)

    def getTree(self):
        for outputs in zip(self.nodes, self.parents, self.lefts, self.rights):
            pprint.pprint("Nodeid:" + str(outputs[0]) +
                          "  Parent:" + str(outputs[1]) +
                          "  Left_Child:" + str(outputs[2]) +
                          "  Right_Sibling:" + str(outputs[3]))

    def getDepth(self, u):
        # 節点番号u の深さを出力する.
        d = 0
        print("Nodeid:" + str(u))
        while self.parents[u] is not None:
            u = self.parents[u]
            d += 1
        print(" => Depth :" + str(d))
        return d

    def setDepth(self, id, depth):
        # 全ての節点の深さを出力する.(節点idのdepth（深さ)を引数と取る.)
        if id == 0:
            self.tmpTable = self.depthTable.copy()

        self.tmpTable[id] = depth
        if self.rights[id] is not None:
            self.setDepth(self.rights[id], depth)
        if self.lefts[id] is not None:
            self.setDepth(self.lefts[id], depth + 1)
        print(self.tmpTable)

    def printChild(self, u):
        # ある節点uの子を全て出力する.
        childTable = []
        printU = u
        if self.lefts[u] is not None:
            childTable.append(self.lefts[u])
            u = self.lefts[u]
            while self.rights[u] is not None:
                childTable.append(self.rights[u])
                u = self.rights[u]
        print("節点番号" + str(printU) + "のChild:" + str(childTable))


# 8.3 二分木の表現
class BinaryTree():
    # 子を必ず２つしか持たないBinary Treeでは,Left = 左の子, Right = 右の子となる.

    def __init__(self):
        self.nodes = []
        self.parents = []
        self.lefts = []
        self.rights = []
        self.depthTable = []
        self.heightTble = []
        self.tmpTable = []

    def insert(self, nodeid, parent=None, left=None, right=None):
        self.nodes.append(nodeid)
        self.parents.append(parent)
        self.lefts.append(left)
        self.rights.append(right)
        self.depthTable.append(None)

    def getTree(self):
        for outputs in zip(self.nodes, self.parents, self.lefts, self.rights):
            pprint.pprint("Nodeid:" + str(outputs[0]) +
                          "  Parent:" + str(outputs[1]) +
                          "  Left_Child:" + str(outputs[2]) +
                          "  Right_Child:" + str(outputs[3]))

    def getDepth(self, u):
        # 節点番号u の深さを出力する.
        d = 0
        print("Nodeid:" + str(u))
        while self.parents[u] is not None:
            u = self.parents[u]
            d += 1
        print(" => Depth :" + str(d))
        return d

    def getHeigth(self, h, u):
        hLeft = hRight = 0

        if self.lefts[u] is not None:
            hLeft = self.getHeigth(h, self.lefts[u]) + 1
        if self.rights[u] is not None:
            hRight = self.getHeigth(h, self.rights[u]) + 1

        if hLeft >= hRight:
            return hLeft
        else:
            return hRight

    def preOrder(self, u):
        # 真ん中→左→右
        if u is None:
            return
        print(u)
        self.preOrder(self.lefts[u])
        self.preOrder(self.rights[u])

    def inOrder(self, u):
        # 左→真ん中→右
        if u is None:
            return
        self.preOrder(self.lefts[u])
        print(u)
        self.preOrder(self.rights[u])

    def postOrder(self, u):
        # 左→右→真ん中
        if u is None:
            return
        self.preOrder(self.lefts[u])
        self.preOrder(self.rights[u])
        print(u)


# 8.4 二分探索木.配列ではなく,クラスを用いて表現.
# 二分探索木は重複を許さないため、SetやMap(Dict)で実装することが出来る.
class Nodes():
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.right = None
        self.left = None


class BinarySearchTree():
    def __init__(self):
        self.nodeList = []  # ポインタ配列...のようなもの.

    def insertFail(self, node):
        # ポインタを用いて実装すべきでした。値でポインタの受け渡しはできない。失敗作。
        # Pythonでは, intはイミュータブルのため、ポインタコピーしようとすると自動的に値渡しになってしまう。。。

        # 初めて作成する場合.
        if not bool(self.nodeList):
            self.nodeList.append(node)
            return

        # 2回目以降の挿入
        p = self.nodeList[0]  # 親を移動していくための変数で最初はトップのノード.本で言うTの根（木の深さが0の地点).
        n = node  # 挿入したいノード.

        # 挿入位置探索
        # 移動前に親を保存しておく. 参照渡しと値渡しに注意.普通に渡すと参照渡しになる.
        while True:

            # 挿入したいノードが親ノードの値より大きい時
            if p.key < n.key:
                if p.right is None:
                    p.right = n.key
                    break

                # ポインタを右へ移動.
                p.key = p.right

            # 挿入したいノードが親ノードの値より小さい時
            else:
                if p.left is None:
                    p.left = n.key
                    break

                # ポインタを左に移動.
                p.key = p.left

        # 子（移動したノード）の親ノードを変更する.
        n.parent = p.key

        # メンバ変数は、クラス名.nodeList でも, self.nodeリストでも呼び出せる.
        self.nodeList.append(n)

    def insert(self, node):
        # Keyは値, right/left/parentはポインタ.

        # 初めて作成する場合.
        if not bool(self.nodeList):
            self.nodeList.append(node)
            return

        # 2回目以降の挿入
        p = self.nodeList[0]  # 親を移動していくための変数で最初はトップのノード.本で言うTの根（木の深さが0の地点).
        n = node  # 挿入したいノード.

        # 挿入位置探索 移動前に親を保存しておく. 参照渡しと値渡しに注意.普通に渡すと参照渡しになる.
        while True:

            # 挿入したいノードが親ノードの値より大きい時
            if p.key < n.key:
                if p.right is None:
                    p.right = n
                    break

                # ポインタを右へ移動.
                p = p.right

            # 挿入したいノードが親ノードの値より小さい時
            else:
                if p.left is None:
                    p.left = n
                    break

                # ポインタを左に移動.
                p = p.left

        # 子（移動したノード）の親ノードを変更する.
        n.parent = p

        # メンバ変数は、クラス名.nodeList でも, self.nodeリストでも呼び出せる.
        self.nodeList.append(n)

    def printtree(self):
        print("Keyはint型, それ以外はポインタを保存してある.")
        pprint.pprint("NodeID" + str([id(x) for x in self.nodeList]))
        pprint.pprint("Key:" + str([x.key for x in self.nodeList]))
        pprint.pprint("Parent:" + str([id(x.parent) for x in self.nodeList]))
        pprint.pprint("Right:" + str([id(x.right) for x in self.nodeList]))
        pprint.pprint("Left:" + str([id(x.left) for x in self.nodeList]))

    def gettreeFail(self, pnode=None):
        # Noneは型であり、Nodeもクラスである。そのため、printをそのまま実行することが不可能.
        # Node.parentはポインタのため、Node.parent.keyとしたいが、None.keyを参照することができない.
        if pnode is None: return
        print(pnode.key, pnode.parent, pnode.right, pnode.left)
        self.gettree(pnode.right)
        self.gettree(pnode.left)

    def gettree(self, pnode=None):
        if pnode is None: return
        print(pnode.key, pnode.parent, pnode.right, pnode.left)
        self.gettree(pnode.right)
        self.gettree(pnode.left)

    def find(self, v):
        p = self.nodeList[0]

        while p is not None :

            if p.key == v:
                return True

            elif p.key < v:
                p = p.right

            elif p.key > v:
                p = p.left

        return False

    def deleteNode(self,n):
        # 削除する対象ノードをyとする.

        if n.left is None or n.right is None: # 子を持たない、または子を一つ持つ.
            y = n
        else:
            pass

        if y.left is not None: # 左の節点の方が値が小さいため、基本的には左を削除ノードの位置に持ってくる.
            x = y.left
        else:
            x = y.right







if __name__ == "__main__":
    # rt = RootedTree()
    # rt.insert(0, None, 1, None)
    # rt.insert(1, 0, 3, 2)
    # rt.insert(2, 0, 4)
    # rt.insert(3, 1, None, 4)
    # rt.insert(4, 2, None, None)
    # rt.getTree()
    # rt.getDepth(3)
    # rt.setDepth(0, 0)
    # rt.printChild(0)

    '''
    bt = BinaryTree()
    bt.insert(0, None, 1, None)
    bt.insert(1, 0, 3, 2)
    bt.insert(2, 0, 4)
    bt.insert(3, 1, None, 4)
    bt.insert(4, 2, None, None)
    bt.getTree()
    bt.getDepth(3)
    bt.getHeigth(0, 1)
    bt.preOrder(0)
    '''

    n1 = Nodes(88)
    n2 = Nodes(35)
    n3 = Nodes(99)
    n4 = Nodes(19)
    bst = BinarySearchTree()
    bst.insert(n1)
    bst.insert(n2)
    bst.insert(n3)
    bst.insert(n4)
    bst.printtree()
    # root = n1
    # bst.gettree(root)
    print(bst.find(35))
    print(bst.find(36))
    # bst.getTree()
    # bst.insert(0, None, 1, None,30)
    # bst.insert(1, 0, 3, 2,88)
    # bst.insert(2, 0, 4)
    # bst.insert(3, 1, None, 4)
    # bst.insert(4, 2, None, None)
    # bst.getTree()
