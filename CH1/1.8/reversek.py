# 把链表以K个结点为一组进行翻转
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

def Reverse(head):
    if head is None or head.next is None:
        return

    cur = head.next
    pre = head
    next = cur.next
    pre.next = None

    while cur is not None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = cur.next
        cur = next

    return pre

def ReverseK(head, k):
    if head is None or head.next is None or k<2:
        return

    i = 1
    pre = head
    begin = head.next
    end = None
    pNext = None

    while begin is not None:
        end = begin

        while i < k:
            if end.next is not None:
                end = end.next
            else:
                return
            i += 1

        pNext = end.next
        end.next = None
        pre.next = Reverse(begin)
        begin.next = pNext
        pre = begin
        begin = pNext
        i = 1

if __name__ == '__main__':
    head = ConstructList()
    print("顺序输出：", end=' ')
    PrintList(head)
    ReverseK(head,3)
    print()
    print("逆序输出：", end=' ')
    PrintList(head)
