def swap(arr,low,high):
    while low < high:
        tmp = arr[low]
        arr[low] = arr[high]
        arr[high] = tmp
        low += 1
        high -= 1

def rotate_arr(arr,div):
    if arr is None or div < 0 or div >= len(arr):
        print("参数错误")
        return
    # 不需要旋转
    if div == 0 or div == len(arr)-1:
        return
    
    swap(arr,0,div)
    swap(arr,div+1,len(arr)-1)
    swap(arr,0,len(arr)-1)


if __name__ == "__main__":
    arr = [1,2,3,4,5]
    rotate_arr(arr,2)
    print(arr)
