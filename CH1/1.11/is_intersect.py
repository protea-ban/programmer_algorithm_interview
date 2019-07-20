"""
判断两个单链表是否交叉，若交叉，给出交叉点的值
"""
class LNode:
    def __init__(self):
        self.data = None
        self.next = None

def IsIntersect(head1, head2):
    if head1 is None or head1.next is None or head2 is None or head2.next is None:
        return None

    temp1 = head1.next
    temp2 = head2.next
    n1, n2 = 0, 0

    while temp1 is not None:
        temp1 = temp1.next
        n1 += 1

    while temp2 is not None:
        temp2 = temp2.next
        n2 += 1

    if temp1 != temp2:
        return None

    if n1 > n2:
        while n1 - n2 > 0:
            head1 = head1.next
            n1 -= 1

    if n2 > n1:
        while n2 - n1 > 0:
            head2 = head2.next
            n2 -= 1

    while head1 != head2:
        head1 = head1.next
        head2 = head2.next

    return head1


if __name__ == '__main__':
    i = 1
    head1 = LNode()
    head1.next = None
    head2 = LNode()
    head2.next = None
    tmp = None
    cur = head1
    p = None

    while i < 8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        if i == 5:
            p = tmp
        i += 1

    cur = head2
    i = 1

    while i < 5:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1

    cur.next = p
    interNode = IsIntersect(head1, head2)
    if interNode is None:
        print("两个链表不相交")
    else:
        print("两个链表相交于：", str(interNode.data))
