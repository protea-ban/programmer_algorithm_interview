# 如何把一个有序整数数组放到二叉树中
# 采用链式存储结构实现二叉树
class BiTNode():
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


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

# 中序遍历
def printTreeMidOrder(root):
    if root is None:
        return

    if root.lchild is not None:
        printTreeMidOrder(root.lchild)

    print(root.data, end=' ')

    if root.rchild is not None:
        printTreeMidOrder(root.rchild)


if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9,10]
    print("原数组：", end=' ')
    for em in arr:
        print(em, end=' ')

    root = array2tree(arr,0,len(arr)-1)
    print("转成树之后的中序遍历：")
    printTreeMidOrder(root)
