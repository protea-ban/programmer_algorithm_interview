
class LNode:
    def __init__(self):
        self.data = None
        self.next = None

def FindMiddleNode(head):
    if head is None or head.next is None:
        return head

    fast = head
    slow = head
    slowPre = head

    while fast is not None and fast.next is not None:
        slowPre = slow
        slow = slow.next
        fast = fast.next.next

    slowPre.next = None
    return slow

def Reverse(head):
    if head is None or head.next is None:
        return head

    pre = head
    cur = head.next
    next = cur.next
    pre.next = None

    while cur is not None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = cur.next
        cur = next

    return pre

def Reorder(head):
    if head is None or head.next is None:
        return

    cur1 = head.next
    mid = FindMiddleNode(head.next)
    cur2 = Reverse(mid)
    tmp = None

    while cur1.next is not None:
        tmp = cur1.next
        cur1.next = cur2
        cur1 = tmp
        tmp = cur2.next
        cur2.next = cur1
        cur2 = tmp

    cur1.next = cur2


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
        i += 1

    print("排序前：", end=' ')
    cur = head.next
    while cur != None:
        print(cur.data, end=' ')
        cur = cur.next

    print()
    print("排序后：", end=' ')
    Reorder(head)
    cur = head.next
    while cur != None:
        print(cur.data, end=' ')
        cur = cur.next
