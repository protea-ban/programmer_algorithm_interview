# 递归删除
class LNode:
    def __init__(self, x):
        self.data = x
        self.next = None

def removeDupRecursion(head):
    if head.next is None:
        return head

    pointer = None
    cur = head

    head.next = removeDupRecursion(head.next)
    pointer = head.next

    while pointer is not None:
        if head.data == pointer.data:
            cur.next = pointer.next
            pointer = cur.next
        else:
            pointer = pointer.next
            cur = cur.next

    return head

def removeDup(head):
    if head == None:
        return

    head.next = removeDupRecursion(head.next)


if __name__ == '__main__':
    i = 1
    head = LNode(i)
    head.next = None
    tmp = None
    cur = head

    while i < 7:
        if i % 2 == 0:
            tmp = LNode(i+1)
        elif i % 3 == 0:
            tmp = LNode(i-2)
        else:
            tmp = LNode(i)
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1

    print("删除前：", end=' ')
    cur = head.next
    while cur != None:
        print(cur.data, end=' ')
        cur = cur.next

    print()
    print("删除后：", end=' ')
    removeDup(head)
    cur = head.next
    while cur != None:
        print(cur.data, end=' ')
        cur = cur.next
