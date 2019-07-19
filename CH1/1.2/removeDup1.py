# 顺序删除
class LNode:
    def __init__(self, x):
        self.data = x
        self.next = None

def removeDup(head):
    if head == None or head.next == None:
        return

    outerCur = head.next
    innerCur = None
    innerPre = None

    while outerCur != None:
        innerCur = outerCur.next
        innerPre = outerCur
        while innerCur != None:
            if outerCur.data == innerCur.data:
                innerPre.next = innerCur.next
                innerCur = innerCur.next
            else:
                innerPre = innerCur
                innerCur = innerCur.next

        outerCur = outerCur.next


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
