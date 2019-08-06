# 如何找到数组中丢失的数
# 异或法
def getNum(arr):
    if arr is None or len(arr) <= 0:
        print("参数错误")
        return -1

    a = arr[0]
    b = 1
    lens = len(arr)
    i = 1

    while i < lens:
        a = a ^ arr[i]
        i += 1
    
    i=2
    while i <= lens + 1:
        b = b ^ i
        i += 1

    return a ^ b


if __name__ == "__main__":
    arr = [1,4,3,2,7,5]
    print(getNum(arr))
