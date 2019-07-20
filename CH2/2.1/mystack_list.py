# 用列表实现栈
class MyStack:
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

if __name__ == '__main__':
    s = MyStack()
    s.push(4)
    s.push(5)
    print("栈顶元素为：", s.top())
    print("栈大小为：", s.size())
    s.pop()
    print("栈顶元素为：", s.top())
    s.pop()
    print("栈顶元素为：", s.top())
    s.pop()
    print("栈顶元素为：", s.top())
