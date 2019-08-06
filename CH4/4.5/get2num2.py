# 如何找到数组中出现奇数次的数
# 异或法
def get2num(arr):
    if arr is None or len(arr) < 1:
        print("参数错误")
        return
    result = 0
    position = 0
    i= 0
    while i < len(arr):
        result ^= arr[i]
        i += 1

    tmpResult = result
    i = result
    while i & 1 == 0:
        position += 1
        i = i >> 1
    
    i = 1
    while i < len(arr):
        if ((arr[i]>>position)&1) == 1:
            result = result^arr[i]

        i += 1
    
    print(result)
    print(result^tmpResult)


if __name__ == "__main__":
    arr = [3,5,6,6,5,7,2,2]
    get2num(arr)
