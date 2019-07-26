# 如何在二叉树中找到路径最大的和
# 采用链式存储结构实现二叉树
class BiTNode():
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


class IntRef():
    def __init__(self):
        self.val = None


def findMaxPathRecursive(root, maxs):
    if root is None:
        return 0
    else:
        sumLeft = findMaxPathRecursive(root.lchild, maxs)
        sumRight = findMaxPathRecursive(root.rchild, maxs)

    allMax = root.data + sumLeft + sumRight
    leftMax = root.data + sumLeft
    rightMax = root.data + sumRight
    tmpMax = max(allMax, leftMax, rightMax)

    if tmpMax > maxs.val:
        maxs.val = tmpMax

    subMax = sumLeft if sumLeft > sumRight else sumRight

    return root.data + subMax

def findMaxPath(root):
    maxs = IntRef()
    maxs.val = -2**31
    findMaxPathRecursive(root, maxs)
    return maxs.val


if __name__ == '__main__':
    root = BiTNode()
    root.data = 2
    left = BiTNode()
    left.data = 3
    right = BiTNode()
    right.data = 5

    root.lchild = left
    root.rchild = right

    print(findMaxPath(root))
