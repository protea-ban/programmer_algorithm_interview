# 逆序输出 递归法
# 就地逆序
class LNode:
    def __init__(self, x):
        self.data = x
        self.next = None

def ReversePrint(firstNode):
    if firstNode is None:
        return
    ReversePrint(firstNode.next)
    print(firstNode.data, end=' ')


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
    # 逆序输出时参数为第一个结点，不是头结点
    ReversePrint(head.next)
