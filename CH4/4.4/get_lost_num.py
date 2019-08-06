# 如何找到数组中丢失的数
# 累加求和
def getNum(arr):
    if arr is None or len(arr) <= 0:
        print("参数不合理")
        return -1
    
    suma = 0
    sumb = 0
    i = 0
    while i < len(arr):
        suma += arr[i]
        sumb += i
        i += 1

    sumb = sumb + len(arr)+len(arr)+1
    
    return sumb - suma


if __name__ == "__main__":
    arr = [1,4,3,2,7,5]
    print(getNum(arr))
