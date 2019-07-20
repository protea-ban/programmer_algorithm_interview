# 把链表相邻元素翻转
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

def reverse(head):
    if head is None or head.next is None:
        return

    cur = head.next
    pre = head
    next = None

    while cur != None and cur.next != None:
        next = cur.next.next
        pre.next = cur.next
        cur.next.next = cur
        cur.next = next
        pre = cur
        cur = next

def PrintList(head):
    cur = head.next
    while cur is not None:
        print(cur.data, end=' ')
        cur = cur.next


if __name__ == '__main__':
    head = ConstructList()
    print("顺序输出：", end=' ')
    PrintList(head)
    reverse(head)
    print()
    print("逆序输出：", end=' ')
    PrintList(head)
