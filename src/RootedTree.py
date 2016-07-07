class RootedTree():
    # Rooted Treeでは,Left = 最も左の子, Right = すぐ右の兄弟とする.
    # Rooted Treeは子を3つ以上持つこともあるため、LeftとRightでは表現できない.
    # 子を２つしか持たないBinary Treeでは,Left = 左の子,    Right = 右の子となる.

    def __init__(self):
        self.nodes = []
        self.parents = []
        self.lefts = []
        self.rights = []

    def insert(self, nodeid, parent=None, left=None, right=None):
        self.nodes.append(nodeid)
        self.parents.append(parent)
        self.lefts.append(left)
        self.rights.append(right)

    def getTree(self):
        for outputs in zip(self.nodes, self.parents, self.lefts, self.rights):
            print("Nodeid:" + str(outputs[0]) +
                  "  Parent:" + str(outputs[1]) +
                  "  Left_Child:" + str(outputs[2]) +
                  "  Right_Sibling:" + str(outputs[3]))

    def getDepth(self, u):
        d = 0
        print("Nodeid:" + str(u))
        while self.parents[u] is not None:
            u = self.parents[u]
            d += 1
        print(" => Depth :" + str(d))
        return d

if __name__ == "__main__":
    t = RootedTree()
    t.insert(0)
    t.insert(1, 0, 3, 2)
    t.insert(2, 0, 4)
    t.insert(3, 1, None, 4)
    t.insert(4, 2, None, None)
    t.getTree()
    t.getDepth(3)