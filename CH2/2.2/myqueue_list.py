# 用列表实现队列
class MyQueue:
    def __init__(self):
        self.arr = []
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear

    def size(self):
        return self.rear - self.front

    def getFront(self):
        if self.isEmpty():
            return None

        return self.arr[self.front]

    def getBack(self):
        if self.isEmpty():
            return None

        return self.arr[self.rear-1]

    def deQueue(self):
        if self.rear > self.front:
            self.front += 1
        else:
            print("队列已空")

    def enQueue(self, item):
        self.arr.append(item)
        self.rear += 1


if __name__ == '__main__':
    queue = MyQueue()
    queue.enQueue(1)
    queue.enQueue(2)
    print("队列头为：", queue.getFront())
    print("队列尾为：", queue.getBack())
    print("队列大小为：", queue.size())
