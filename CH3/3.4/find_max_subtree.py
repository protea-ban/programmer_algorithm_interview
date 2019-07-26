# 如何求一棵二叉树的最大子树和
# 采用链式存储结构实现二叉树
class BiTNode():
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


class Test():
    def __init__(self):
        self.maxSum = -2**31

    def constructTree(self):
        root = BiTNode()
        node1 = BiTNode()
        node2 = BiTNode()
        node3 = BiTNode()
        node4 = BiTNode()

        root.data = 6
        node1.data = 3
        node2.data = -7
        node3.data = -1
        node4.data = 9
        root.lchild = node1
        root.rchild = node2
        node1.lchild = node3
        node1.rchild = node4

        return root

    def findMaxSubTree(self, root, maxRoot):
        if root is None:
            return 0

        lmax = self.findMaxSubTree(root.lchild, maxRoot)
        rmax = self.findMaxSubTree(root.rchild, maxRoot)
        sums = lmax + rmax + root.data

        if sums > self.maxSum:
            self.maxSum = sums
            maxRoot.data = root.data

        return sums


if __name__ == '__main__':
    test = Test()
    root = test.constructTree()
    maxRoot = BiTNode()
    test.findMaxSubTree(root, maxRoot)
    print("最大子树和：", test.maxSum)
    print("对应子树的根节点：", maxRoot.data)
