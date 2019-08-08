# 如何求数组连续最大和
# 动态规划法
def maxSubArray(arr):
    if arr is None or len(arr) < 1:
        print("参数不合法")
        return
    n = len(arr)
    End = [None]*n
    All = [None] * n
    All[n-1] = End[n-1] = arr[n-1]
    End[0] = All[0] = arr[0]
    i = 1
    while i < n:
        End[i] = max(End[i-1]+arr[i], arr[i])
        All[i] = max(End[i], All[i-1])
        i += 1
    
    return All[n-1]


if __name__ == "__main__":
    arr = [1,-2,4,8,-4,7,-1,-5]
    print("连续最大和为：", maxSubArray(arr))
