# 如何求数组中两个元素的最小距离
# 蛮力法 双重遍历
def minDistance(arr,num1,num2):
    if arr is None or len(arr) < 0:
        print("参数不合理")
        return 2**32

    minDis = 2 ** 32
    dist = 0
    i = 0
    while i < len(arr):
        if arr[i] == num1:
            j = 0
            while j < len(arr):
                if arr[j] == num2:
                    dist = abs(i-j)
                    if dist < minDis:
                        minDis = dist
                
                j += 1

        i += 1

    return minDis


if __name__ == "__main__":
    arr = [4,5,6,4,7,4,7,4,7,8,5,6,4,3,10,8]
    num1 = 4
    num2 = 8
    print(minDistance(arr,num1,num2))