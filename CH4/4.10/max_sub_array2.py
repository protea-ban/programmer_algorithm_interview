# 如何求数组连续最大和
# 重复利用已经计算的子数组和
def maxSubArray(arr):
    if arr is None or len(arr) < 1:
        print("参数不合法")
        return
    
    maxSum = -2 ** 32
    i = 0
    while i < len(arr):
        sums = 0
        j = i
        while j < len(arr):
            sums += arr[j]
            if sums > maxSum:
                maxSum = sums
            j += 1
        i += 1

    return maxSum


if __name__ == "__main__":
    arr = [1,-2,4,8,-4,7,-1,-5]
    print("连续最大和为：", maxSubArray(arr))
