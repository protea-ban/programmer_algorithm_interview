# 链表存在环，找出环的入口点
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

    cur.next = head.next.next.next
    return head

def isLoop(head):
    if head is None or head.next is None:
        return None

    slow = head.next
    fast = head.next

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return slow

    return None

def findLoopNode(head, meetNode):
    first = head.next
    second = meetNode

    while first != second:
        first = first.next
        second = second.next

    return first


if __name__ == '__main__':
    head = ConstructList()
    meetNode = isLoop(head)
    loopNode = None
    if meetNode is not None:
        print("有环")
        loopNode = findLoopNode(head, meetNode)
        print("环的入口为：", str(loopNode.data))
    else:
        print("无环")
