# 如何对数组进行循环移位，要求时间复杂度为O(N),只允许使用两个附加变量
# 三步翻转法：分为两部分，分别翻转，然后整体进行翻转
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def right_shift(arr,k):
    if arr is None:
        print("参数不合法")
        return
    lens = len(arr)
    k %= lens
    reverse(arr,0,lens-k-1)
    reverse(arr,lens-k,lens-1)
    reverse(arr,0,lens-1)

if __name__ == "__main__":
    k = 4
    arr = [1,2,3,4,5,6,7,8]
    right_shift(arr,k)
    i = 0
    print(arr)
