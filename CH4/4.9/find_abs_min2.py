# 如何求数组中绝对值最小的数
# 二分法
def finMin(array):
    if array is None or len(array) <=0 :
        print("参数不合理")
        return 

    lens = len(array)

    if array[0] >= 0:
        return array[0]

    if array[lens-1] <= 0:
        return array[lens-1]
    
    mid = 0
    begin = 0
    end = lens - 1
    absMin = 0

    while True:
        mid = begin + (end-begin) // 2
        if array[mid] == 0:
            return 0
        elif array[mid] > 0:
            if array[mid-1] > 0:
                end = mid -1
            elif array[mid-1] == 0:
                return 0
            else:
                break
        else:
            if array[mid+1] < 0:
                begin = mid + 1
            elif array[mid+1] == 0:
                return 0
            else:
                break

    if array[mid] > 0:
        if array[mid] < abs(array[mid-1]):
            absMin = array[mid]
        else:
            absMin = array[mid-1]
    else:
        if abs(array[mid]) < array[mid+1]:
            absMin = array[mid]
        else:
            absMin = array[mid+1]

    return absMin


if __name__ == "__main__":
    arr = [-10,-5,-2,7,15,20]
    print("绝对值最小的元素为",finMin(arr))
