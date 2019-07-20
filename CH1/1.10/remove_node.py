# 在只给定单链表中某个结点的指针的情况下删除该结点
class LNode:
    def __init__(self):
        self.data = None
        self.next = None

# 构造单链表
def ConstructList():
    i = 1
    head = LNode()
    head.next = None
    tmp = None
    cur = head

    while i < 8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1

    return head

# 遍历打印链表
def PrintList(head):
    cur = head.next
    while cur is not None:
        print(cur.data, end=' ')
        cur = cur.next

def Remove(pow):
    if p is None or p.next is None:
        return False

    p.data = p.next.data
    tmp = p.next
    p.next = tmp.next

    return True


if __name__ == '__main__':
    i = 1
    head = LNode()
    head.next = None
    tmp = None
    cur = head

    while i < 8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        if i == 5:
            p = tmp
        i += 1

    print("顺序输出：", end=' ')
    PrintList(head)
    result = Remove(p)
    if result:
        print("删除成功")
    PrintList(head)
