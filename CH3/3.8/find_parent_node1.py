# 如何找出排序二叉树上任意两个结点的最近共同父结点
# 方法一：路径对比法
# 采用链式存储结构实现二叉树
class BiTNode():
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

    def __str__(self):
        return str(self.data)


# 用列表实现栈
class MyStack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def top(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]
        else:
            return None

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            print("栈已空")
            return None

    def push(self, item):
        self.items.append(item)


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
    stack1 = MyStack()
    stack2 = MyStack()
    getPathFromRoot(root,node1,stack1)
    getPathFromRoot(root, node2, stack2)
    commonParent = None

    while stack1.top() == stack2.top():
        commonParent = stack1.top()
        stack1.pop()
        stack2.pop()

    return commonParent

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
