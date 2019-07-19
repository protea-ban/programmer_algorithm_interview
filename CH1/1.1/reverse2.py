# 递归法
class LNode:
    def __init__(self, x):
        self.data = x
        self.next = None

def RecursiveReverse(head):
    if head is None or head.next is None:
        return head
    else:
        newhead = RecursiveReverse(head.next)
        head.next.next = head
        head.next = None

    return newhead

def Reverse(head):
    if head is None:
        return

    firstNode = head.next
    newhead = RecursiveReverse(firstNode)
    head.next = newhead
    return newhead


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
