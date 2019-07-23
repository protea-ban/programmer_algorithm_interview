# 用两个栈来模拟队列操作
# 基本栈
class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def top(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]
        else:
            return None

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            print("栈已空")
            return None

    def push(self, item):
        self.items.append(item)


class MyStack():
    def __init__(self):
        self.A = Stack()
        self.B = Stack()

    def push(self, data):
        self.A.push(data)

    def pop(self):
        if self.B.isEmpty():
            while not self.A.isEmpty():
                self.B.push(self.A.top())
                self.A.pop()

        first = self.B.top()
        self.B.pop()

        return first


if __name__ == '__main__':
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("队列的队首元素为：",stack.pop())
    print("队列的队首元素为：",stack.pop())
    print("队列的队首元素为：",stack.pop())
