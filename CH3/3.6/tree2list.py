# 如何把二叉树转换成双向链表
# 采用链式存储结构实现二叉树
class BiTNode():
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


class Test():
    def __init__(self):
        self.pHead = None
        self.pEnd = None

    def array2tree(self, arr, start, end):
        root = None
        if end >= start:
            root = BiTNode()
            mid = (start+end+1) // 2
            root.data = arr[mid]
            root.lchild = self.array2tree(arr, start, mid-1)
            root.rchild = self.array2tree(arr, mid+1, end)
        else:
            root = None

        return root

    def inOrderBSTree(self, root):
        if root is None:
            return

        self.inOrderBSTree(root.lchild)
        root.lchild = self.pEnd
        if self.pEnd is None:
            self.pHead = root
        else:
            self.pEnd.rchild = root

        self.pEnd = root
        self.inOrderBSTree(root.rchild)


if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7]
    test = Test()
    root = test.array2tree(arr,0,len(arr)-1)
    test.inOrderBSTree(root)
    cur = test.pHead
    while cur is not None:
        print(cur.data, end=' ')
        cur = cur.rchild

    cur = test.pEnd
    while cur is not None:
        print(cur.data, end=' ')
        cur = cur.lchild
