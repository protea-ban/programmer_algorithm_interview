# 如何在二叉树中找到与输入整数相等的所有路径
# 采用链式存储结构实现二叉树
class BiTNode():
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


def constructTree():
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

def findRoad(root,num,sums,v):
    sums += root.data
    v.append(root.data)
    if root.lchild is None and root.rchild is None and sums == num:
        for item in v:
            print(item, end=' ')
        print()

    if root.lchild is not None:
        findRoad(root.lchild, num, sums, v)

    if root.rchild is not None:
        findRoad(root.rchild, num, sums, v)

    # 清除遍历的路径
    sums -= v[-1]
    v.remove(v[-1])


if __name__ == '__main__':
    root = constructTree()
    s = []
    findRoad(root,8,0,s)
