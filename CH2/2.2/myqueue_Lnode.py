# 用链表实现队列
class LNode:
    def __init__(self):
        self.data = None
        self.next = None

class MyQueue:
    def __init__(self):
        self.pHead = None
        self.pEnd = None

    def isEmpty(self):
        if self.pHead is None:
            return True
        else:
            return False

    def size(self):
        size = 0
        p = self.pHead
        while p is not None:
            p = p.next
            size += 1

        return size

    def enQueue(self, e):
        p = LNode()
        p.data = e
        p.next = None

        if self.pHead is None:
            self.pHead = self.pEnd = p
        else:
            self.pEnd.next = p
            self.pEnd = p

    def deQueue(self):
        if self.pHead is None:
            print("队列已空")
        self.pHead = self.pHead.next
        if self.pHead is None:
            self.pEnd is None

    def getFront(self):
        if self.pHead is None:
            print("队列为空，无法获取")
            return None

        return self.pHead.data

    def getBack(self):
        if self.pHead is None:
            print("队列为空，获取失败")
            return None

        return self.pEnd.data


if __name__ == '__main__':
    queue = MyQueue()
    queue.enQueue(1)
    queue.enQueue(2)
    print("队列头为：", queue.getFront())
    print("队列尾为：", queue.getBack())
    print("队列大小为：", queue.size())
