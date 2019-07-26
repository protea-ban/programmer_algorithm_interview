# 如何找出排序二叉树上任意两个结点的最近共同父结点
# 方法二：结点编号法,性质：编号为i的父结点编号为i/2
# ############################## 有问题 ##################################
import math
# 采用链式存储结构实现二叉树
class BiTNode():
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

    def __str__(self):
        return str(self.data)

# 有序数组转成二叉树
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

class IntRef():
    def __init__(self):
        self.num = None


def getNo(root, node, number):
    if root is None:
        return False
    if root == node:
        return True
    tmp = number.num
    number.num = 2 * tmp
    if getNo(root.lchild, node,number):
        return True
    else:
        number.num = tmp * 2 + 1
        return getNo(root.rchild, node, number)

def getNodeFromNum(root,number):
    if root is None or number < 0:
        return None

    if number == 1:
        return root
    lens = int((math.log(number))/(math.log(2)))
    number -= 1 << lens
    print("number:", number)
    while lens > 0:
        if ((1 << (lens-1)) and number) == 1:
            root = root.rchild
        else:
            root = root.lchild
        lens -= 1

    return root

def FindParentNode(root, node1, node2):
    ref1 = IntRef()
    ref1.num = 1
    ref2 = IntRef()
    ref2.num = 1
    getNo(root, node1, ref1)
    getNo(root, node2, ref2)
    num1 = ref1.num
    num2 = ref2.num
    while num1 != num2:
        if num1 > num2:
            num1 /= 2
        else:
            num2 /= 2

    return getNodeFromNum(root, num1)


if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9,10]
    root = array2tree(arr, 0, len(arr)-1)
    node1 = root.lchild.lchild.lchild
    node2 = root.lchild.lchild
    res = None
    res = FindParentNode(root, node1, node2)
    if res is not None:
        print("最近公共父结点是：",res.data)
    else:
        print("没有共同父结点")
