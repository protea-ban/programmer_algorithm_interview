"""
找出单链表中的倒数第K个元素
"""
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

def PrintList(head):
    cur = head.next
    while cur is not None:
        print(cur.data, end=' ')
        cur = cur.next

def FindLastK(head, k):
    if head is None or head.next is None:
        return head

    slow = LNode()
    fast = LNode()
    slow = head.next
    fast = head.next
    i = 0

    while i < k and fast is not None:
        fast = fast.next
        i += 1

    if i < k:
        return None

    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow

def MyFindLastK(head, k):
    if head is None or head.next is None:
        return head

    slow = LNode()
    fast = LNode()
    slow = head.next
    fast = head.next
    i = 0

    while k > 0:
        fast = fast.next
        k -= 1

    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow


if __name__ == '__main__':
    head = ConstructList()
    print("链表：", end=' ')
    PrintList(head)
    result = MyFindLastK(head, 3)
    if result is not None:
        print("\n", result.data)
