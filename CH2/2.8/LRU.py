# 如何实现LRU缓存方案
from collections import deque

class LRU():
    def __init__(self, chacheSize):
        self.chacheSize = chacheSize
        self.queue = deque()
        self.hashSet = set()

    def isFull(self):
        return len(self.queue) == self.chacheSize

    def enQueue(self, pageNum):
        if self.isFull():
            self.hashSet.remove(self.queue[-1])
            self.queue.pop()

        self.queue.appendleft(pageNum)
        self.hashSet.add(pageNum)

    def accessPage(self,pageNum):
        # 不在缓存队列中，page放到队首
        if pageNum not in self.hashSet:
            self.enQueue(pageNum)
        elif pageNum != self.queue[0]:
            self.queue.remove(pageNum)
            self.queue.appendleft(pageNum)

    def printQueue(self):
        while len(self.queue) > 0:
            print(self.queue.popleft())


if __name__ == '__main__':
    lru = LRU(3)
    lru.accessPage(1)
    lru.accessPage(2)
    lru.accessPage(5)
    lru.accessPage(1)
    lru.accessPage(6)
    lru.accessPage(7)
    lru.printQueue()
