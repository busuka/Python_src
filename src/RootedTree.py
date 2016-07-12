import pprint


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
        # 全ての節点の深さを出力する.(節点idのdepthを引数と取る.)
        if id == 0:
            self.tmpTable = self.depthTable.copy()

        self.tmpTable[id] = depth
        if self.rights[id] is not None:
            self.setDepth(self.rights[id], depth)
        if self.lefts[id] is not None:
            self.setDepth(self.lefts[id], depth + 1)
        print(self.tmpTable)

    def printChild(self, u):
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

    def preOrder(self,u):
        # 真ん中→左→右
        if u is None:
            return
        print(u)
        self.preOrder(self.lefts[u])
        self.preOrder(self.rights[u])

    def inOrder(self,u):
        # 左→真ん中→右
        if u is None:
            return
        self.preOrder(self.lefts[u])
        print(u)
        self.preOrder(self.rights[u])

    def postOrder(self,u):
        # 左→右→真ん中
        if u is None:
            return
        self.preOrder(self.lefts[u])
        self.preOrder(self.rights[u])
        print(u)


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
