# 如何对二叉树链表进行镜像反转

from collections import deque
# 采用链式存储结构实现二叉树
class BiTNode():
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

def reverseTree(root):
    if root is None:
        return

    reverseTree(root.lchild)
    reverseTree(root.rchild)
    tmp = root.lchild
    root.lchild = root.rchild
    root.rchild = tmp

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

def travsing_tree_layer(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        p = queue.popleft()
        print(p.data, end=' ')

        if p.lchild is not None:
            queue.append(p.lchild)

        if p.rchild is not None:
            queue.append(p.rchild)


if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7]
    root = array2tree(arr, 0, len(arr)-1)
    travsing_tree_layer(root)
    print()
    reverseTree(root)
    travsing_tree_layer(root)
