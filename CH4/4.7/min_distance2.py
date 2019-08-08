# 如何求数组中两个元素的最小距离
# 动态规划
def minDistance(arr,num1,num2):
    if arr is None or len(arr) < 0:
        print("参数不合理")
        return 2 ** 32
    
    lastPos1 = -1
    lastPos2 = -1
    minDis = 2 ** 32
    i = 0

    while i < len(arr):
        if arr[i] == num1:
            lastPos1 = i
            if lastPos2 >= 0:
                minDis = min(minDis, lastPos1-lastPos2)
        if arr[i] == num2:
            lastPos2 = i
            if lastPos1 >= 0:
                minDis = min(minDis, lastPos2 - lastPos1)
        
        i += 1

    return minDis


if __name__ == "__main__":
    arr = [4,5,6,4,7,4,7,4,7,8,5,6,4,3,10,8]
    num1 = 4
    num2 = 8
    print(minDistance(arr,num1,num2))