# 查找数组中元素的最大值和最小值
# 分治法
class MaxMin():
    def __init__(self):
        self.max = None
        self.min = None

    def getMax(self):
        return self.max

    def getMin(self):
        return self.min

    def getMaxAndMin(self, arr):
        if arr is None:
            print("参数错误")
            return

        lens = len(arr)
        self.max = arr[0]
        self.min = arr[0]

        # 两两分组，左大右小
        i = 0
        while i < (lens-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
            i += 2

        # 分组左边找最小值
        self.min = arr[0]
        i = 2
        while i < lens:
            if arr[i] < self.min:
                self.min = arr[i]

            i += 2

        # 分组右边找最大值
        self.max = arr[1]
        i = 3
        while i < lens:
            if arr[i] > self.max:
                self.max = arr[i]
            i += 2

        # 如果为奇数，最后一个特殊处理
        if lens % 2 == 1:
            if self.max < arr[lens-1]:
                self.max = arr[lens-1]

            if self.min > arr[lens-1]:
                self.min = arr[lens-1]


if __name__ == '__main__':
    arr = [7,3,19,40,4,7,1]
    m = MaxMin()
    m.getMaxAndMin(arr)
    print("Max", m.getMax())
    print("Min", m.getMin())
