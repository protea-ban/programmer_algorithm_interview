# 如何求数组连续最大和
# 优化的动态规划法
def maxSubArray(arr):
    if arr is None or len(arr) < 1:
        print("参数不合法")
        return
    n = len(arr)
    nAll = arr[0]
    nEnd = arr[0]
    i = 1
    while i < n:
        nEnd = max(nEnd+arr[i],arr[i])
        nAll = max(nEnd,nAll)
        i += 1
    
    return nAll


if __name__ == "__main__":
    arr = [1,-2,4,8,-4,7,-1,-5]
    print("连续最大和为：", maxSubArray(arr))
