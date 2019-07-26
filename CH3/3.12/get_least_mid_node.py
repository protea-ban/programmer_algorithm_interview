# 如何在二叉排序树中找到第一个大于中间值的结点
# 采用链式存储结构实现二叉树
class BiTNode():
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


# 求最小结点，因为是排序二叉树，所以最小结点在最左子树上
def getMidNode(root):
    if root is None:
        return root

    while root.lchild is not None:
        root = root.lchild

    return root

def getMaxNode(root):
    if root is None:
        return root

    while root.rchild is not None:
        root = root.rchild

    return root

def getNode(root):
    maxNode = getMaxNode(root)
    mindNode = getMidNode(root)
    mid = (maxNode.data + mindNode.data) // 2
    result = None
    while root is not None:
        if root.data <= mid:
            root = root.rchild
        else:
            result = root
            root = root.lchild

    return result

def array2tree(arr, start, end):
    root = None
    if end >= start:
        root = BiTNode()
        mid = (start+end+1) // 2
        root.data = arr[mid]
        root.lchild = array2tree(arr, start, mid-1)
        root.rchild = array2tree(arr, mid+1, end)
    else:
        root = None

    return root


if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7]
    root = array2tree(arr,0,len(arr)-1)
    print(getNode(root).data)
