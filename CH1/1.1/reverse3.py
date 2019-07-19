# 插入法逆序
class LNode:
    def __init__(self, x):
        self.data = x
        self.next = None

def Reverse(head):
    if head == None or head.next == None:
        return

    cur = None
    next = None

    cur = head.next.next
    head.next.next = None

    while cur is not None:
        next = cur.next
        cur.next = head.next
        head.next = cur
        cur = next


if __name__ == '__main__':
    i = 1
    head = LNode(i)
    head.next = None
    tmp = None
    cur = head

    while i < 8:
        tmp = LNode(i)
        # tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1

    print("逆序前：", end=' ')
    cur = head.next
    while cur != None:
        print(cur.data, end=' ')
        cur = cur.next

    print()
    print("逆序后：", end=' ')
    Reverse(head)
    cur = head.next
    while cur != None:
        print(cur.data, end=' ')
        cur = cur.next
