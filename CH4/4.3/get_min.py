# 如何找到旋转数组的最小值
# 二分法
def getMin_1(arr,low,high):
    # 旋转个数为0，返回第一个
    if high < low:
        return arr[0]
    # 只剩下一个，肯定为最小值
    if high == low:
        return arr[low]
    
    mid = (low + high) // 2

    if arr[mid] < arr[mid-1]:
        return arr[mid]
    elif arr[mid+1] < arr[mid]:
        return arr[mid+1]
    elif arr[high] > arr[mid]:
        return getMin_1(arr,low,mid-1)
    elif arr[mid] > arr[low]:
        return getMin_1(arr,mid+1,high)
    else:
        return min(getMin_1(arr,low,mid-1), getMin_1(arr,mid+1,high))

def getMin(arr):
    if arr is None:
        print("参数错误")
        return
    else:
        return getMin_1(arr,0,len(arr)-1)


if __name__ == "__main__":
    # arr1 = [5,6,1,2,3,4]
    arr1 = [1,1,0,1]
    mins = getMin(arr1)
    print(mins)

    
