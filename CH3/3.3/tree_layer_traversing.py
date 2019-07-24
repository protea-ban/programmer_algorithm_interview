# 层序遍历二叉树
from collections import deque
# 采用链式存储结构实现二叉树
class BiTNode():
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


# 把有序数组转换为二叉树
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
    arr = [1,2,3,4,5,6,7,8,9,10]
    root = array2tree(arr, 0, len(arr)-1)
    travsing_tree_layer(root)
