# 如何在不排序的情况下求数组中的中位数
# 使用分治思想，寻求一种类似快速排序的方法

class Test():
    def __init__(self):
        self.pos = 0
    
    def partition(self,arr,low,high):
        key = arr[low]
        while low < high:
            while low < high and arr[high] > key:
                high -= 1
            arr[low] = arr[high]
            while low < high and arr[low] < key:
                low += 1
            arr[high] = key
            self.pos = low
    
    def get_mid(self,arr):
        low = 0
        n = len(arr)
        high = n - 1
        mid = (low+high) // 2
        while True:
            self.partition(arr,low,high)
            if self.pos == mid:
                break
            elif self.pos > mid:
                high = self.pos -1
            else:
                low = self.pos + 1
        
        return arr[mid] if (n % 2) != 0 else (arr[mid]+arr[mid+1]) // 2


if __name__ == "__main__":
    arr = [7,5,3,1,11,9]
    test = Test()
    print(test.get_mid(arr))

