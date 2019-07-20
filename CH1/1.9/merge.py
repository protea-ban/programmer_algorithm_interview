# 合并两个有序链表
class LNode:
    def __init__(self):
        self.data = None
        self.next = None

# 构造单链表
def ConstructList(start):
    i = start
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
        i += 2

    return head

# 遍历打印链表
def PrintList(head):
    cur = head.next
    while cur is not None:
        print(cur.data, end=' ')
        cur = cur.next

def Merge(head1, head2):
    if head1 is None or head1.next is None:
        return head2

    if head2 is None or head2.next is None:
        return head1

    cur1 = head1.next
    cur2 = head2.next
    head = None
    cur = None

    if cur1.data > cur2.data:
        head = head2
        cur = cur2
        cur2 = cur2.next
    else:
        head = head1
        cur = cur1
        cur1 = cur1.next

    while cur1 is not None and cur2 is not None:
        if cur1.data < cur2.data:
            cur.next = cur1
            cur = cur1
            cur1 = cur1.next
        else:
            cur.next = cur2
            cur = cur2
            cur2 = cur2.next

    if cur1 is not None:
        cur.next = cur1

    if cur2 is not None:
        cur.next = cur2

    return head


if __name__ == '__main__':
    head1 = ConstructList(1)
    print("head1:", end=' ')
    PrintList(head1)
    head2 = ConstructList(2)
    print()
    print("head2:", end=' ')
    PrintList(head2)
    head = Merge(head1, head2)
    print()
    print("merge:", end=' ')
    PrintList(head)
