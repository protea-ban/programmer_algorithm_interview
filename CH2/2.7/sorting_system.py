# 如何设计一个排序系统
from collections import deque

class User():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.seq = 0

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getSeq(self):
        return self.id

    def setSeq(self, seq):
        self.seq = seq

    def getId(self):
        return self.id

    def equals(self, arg0):
        o = arg0
        return self.id == o.getId()

    def toString(self):
        return "id:{} name:{} seq:{}".format(self.id, self.name, self.seq)


class MyQueue():
    def __init__(self):
        self.q = deque()

    def enQueue(self,u):
        u.setSeq(len(self.q)+1)
        self.q.append(u)

    def deQueue(self):
        self.q.popleft()
        self.updateSeq()

    def deQueuemove(self, u):
        self.q.remove(u)
        self.updateSeq()

    def updateSeq(self):
        i = 1
        for u in self.q:
            u.setSeq(i)
            i += 1

    def printList(self):
        for u in self.q:
            print(u.toString())

if __name__ == '__main__':
    u1 = User(1, "user1")
    u2 = User(2, "user2")
    u3 = User(3, "user3")
    u4 = User(4, "user4")

    queue = MyQueue()
    queue.enQueue(u1)
    queue.enQueue(u2)
    queue.enQueue(u3)
    queue.enQueue(u4)
    queue.deQueue()
    queue.deQueuemove(u3)
    queue.printList()
