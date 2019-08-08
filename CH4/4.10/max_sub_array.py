# 如何求数组连续最大和
# 蛮力法
def maxSubArray(arr):
    if arr is None or len(arr) < 1:
        print("参数不合法")
        return
    
    thisSum = maxSum = 0
    i = 0
    lens = len(arr)
    while i < lens:
        j = i
        while j < lens:
            thisSum = 0
            k = i
            while k < j:
                thisSum += arr[k]
                k += 1
            if thisSum > maxSum:
                maxSum = thisSum
            
            j += 1
        i += 2
    return maxSum


if __name__ == "__main__":
    arr = [1,-2,4,8,-4,7,-1,-5]
    print("连续最大和为：", maxSubArray(arr))
