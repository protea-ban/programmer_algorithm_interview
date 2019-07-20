# 用链表实现栈
class LNode:
    def __init__(self):
        self.data = None
        self.next = None

class MyStack:
    def __init__(self):
        self.data = None
        self.next = None

    def isEmpty(self):
        if self.next is None:
            return True
        else:
            return False

    def size(self):
        size = 0
        p = self.next
        while p != None:
            p = p.next
            while p != None:
                p = p.next
                size += 1

        return size

    def push(self, e):
        p = LNode()
        p.data = e
        p.next = self.next
        self.next = p

    def pop(self):
        tmp = self.next
        if tmp != None:
            self.next = tmp.next
            return tmp.data

        print("栈已空")
        return None

    def top(self):
        if self.next != None:
            return self.next.data

        print("栈已空")
        return None

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
