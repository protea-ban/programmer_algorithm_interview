# 如何找出数组中出现为1次的数
# 判断数字n的二进制数从右向左数第i位是否为1
def isOne(n,i):
    return (n&(1<<i)) == 1

def findSingle(arr):
    size = len(arr)
    i = 0
    while i < 32:
        result1 = result0 = count1 = count0 = 0
        j = 0
        while j < size:
            if isOne(arr[j], i):
                result1 ^= arr[j]
                count1 += 1
            else:
                result0 ^= arr[j]
                count0 += 1
            j += 1
        i += 1
        
        if count1 % 2 == 1 and result0 != 0:
            return result1
        if count0 % 2 == 1 and result1 != 0:
            return result0

    return -1


if __name__ == "__main__":
    arr = [6,3,4,5,9,4,3]
    result = findSingle(arr)
    if result != -1:
        print(result)
    else:
        print("不存在")