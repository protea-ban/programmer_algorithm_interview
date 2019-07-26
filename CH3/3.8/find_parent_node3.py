# 如何找出排序二叉树上任意两个结点的最近共同父结点
# 方法三：后序遍历法
# 采用链式存储结构实现二叉树
class BiTNode():
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

    def __str__(self):
        return str(self.data)

def getPathFromRoot(root,node,s):
    if root is None:
        return False
    if root == node:
        s.push(root)
        return True

    if getPathFromRoot(root.lchild, node, s) or getPathFromRoot(root.rchild, node, s):
        s.push(root)
        return True

    return False

def FindParentNode(root, node1, node2):
    if root is None or root == node1 or root == node2:
        return root

    lchild = FindParentNode(root.lchild, node1, node2)
    rchild = FindParentNode(root.rchild, node1, node2)

    if lchild is None:
        return rchild
    elif rchild is None:
        return lchild
    else:
        return root

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
    arr = [1,2,3,4,5,6,7,8,9,10]
    root = array2tree(arr, 0, len(arr)-1)
    node1 = root.lchild.lchild.lchild
    node2 = root.lchild.lchild
    res = None
    res = FindParentNode(root, node1, node2)
    if res is not None:
        print("最近公共父结点是：",res)
        # print("最近公共父结点是：",res.data) # 有__str__函数返回data了，就不需要res.data
    else:
        print("没有共同父结点")
