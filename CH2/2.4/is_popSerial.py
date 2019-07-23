# 如何根据入栈顺序判断可能的出栈序列
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


def isPopSerial(push, pop):
    if push is None or pop is None:
        return False

    pushLen = len(push)
    popLen = len(pop)

    if pushLen != popLen:
        return False

    pushIndex = 0
    popIndex = 0
    stack = MyStack()

    while pushIndex < pushLen:
        stack.push(push[pushIndex])
        pushIndex += 1

        while (not stack.isEmpty()) and stack.top() == pop[popIndex]:
            stack.pop()
            popIndex += 1

    return stack.isEmpty() and popIndex == popLen


if __name__ == '__main__':
    push = "12345"
    pop = "32541"
    if isPopSerial(push, pop):
        print("YES")
    else:
        print("NO")
