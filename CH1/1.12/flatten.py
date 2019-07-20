"""
带副链表的有序链表扁平化
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None


class MergeList:
    def __init__(self):
        self.head = None

    # 递归合并两个有序的链表，合并后的链表是向下走的
    def merge(self, a, b):
        if a is None:
            return b

        if b is None:
            return a

        if a.data < b.data:
            result = a
            result.down = self.merge(a.down, b)
        else:
            result = b
            result.down = self.merge(a, b.down)

        return result

    def flatten(self, root):
        if root is None or root.right is None:
            return root

        root.right = self.flatten(root.right)
        root = self.merge(root, root.right)

        return root

    # 插入操作，将新结点插入到表头
    def insert(self, head_ref, data):
        new_node = Node(data)
        new_node.down = head_ref
        head_ref = new_node

        # 返回新表头结点
        return head_ref

    # 打印链表
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.down


if __name__ == '__main__':
    L = MergeList()
    L.head = L.insert(L.head, 31)
    L.head = L.insert(L.head, 8)
    L.head = L.insert(L.head, 6)
    L.head = L.insert(L.head, 3)
    L.head.right = L.insert(L.head.right, 21)
    L.head.right = L.insert(L.head.right, 11)
    L.head.right.right = L.insert(L.head.right.right, 50)
    L.head.right.right = L.insert(L.head.right.right, 22)
    L.head.right.right = L.insert(L.head.right.right, 15)
    L.head.right.right.right = L.insert(L.head.right.right.right, 55)
    L.head.right.right.right = L.insert(L.head.right.right.right, 40)
    L.head.right.right.right = L.insert(L.head.right.right.right, 39)
    L.head.right.right.right = L.insert(L.head.right.right.right, 30)
    L.head = L.flatten(L.head)
    L.printList()
