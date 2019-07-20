# 给栈排序，在翻转的算法中的交换栈顶元素与子栈顶元素时增加一步判断即可
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

def moveBottomToTop(s):
    if s.isEmpty():
        return

    top1 = s.top()
    s.pop()

    if not s.isEmpty():
        moveBottomToTop(s)
        top2 = s.top()

        if top1 > top2:
            s.pop()
            s.push(top1)
            s.push(top2)
            return
    s.push(top1)

def reverse_stack(s):
    if s.isEmpty():
        return
    moveBottomToTop(s)
    top = s.top()
    s.pop()
    reverse_stack(s)
    s.push(top)


if __name__ == '__main__':
    s = MyStack()
    s.push(5)
    s.push(6)
    s.push(3)
    s.push(9)
    s.push(1)
    reverse_stack(s)
    while not s.isEmpty():
        print(s.top(), end=' ')
        s.pop()
