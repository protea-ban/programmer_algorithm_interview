# 如何用O(1)的时间复杂度求栈中最小元素
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


class MyStack:
    def __init__(self):
        self.elemStack = Stack()
        self.minStack = Stack()

    def pop(self):
        topData = self.elemStack.top()
        self.elemStack.pop()
        if topData == self.mins():
            self.minStack.pop()

        return topData

    def push(self, data):
        self.elemStack.push(data)
        if self.minStack.isEmpty():
            self.minStack.push(data)
        elif data < self.minStack.top():
            self.minStack.push(data)

    def mins(self):
        if self.minStack.isEmpty():
            return 2**32
        else:
            return self.minStack.top()


if __name__ == '__main__':
    stack = MyStack()
    stack.push(5)
    print("栈中最小值为：", stack.mins())
    stack.push(6)
    print("栈中最小值为：", stack.mins())
    stack.push(4)
    print("栈中最小值为：", stack.mins())
    stack.push(1)
    print("栈中最小值为：", stack.mins())
    stack.push(3)
    print("栈中最小值为：", stack.mins())
