# O(N)时间复杂度内查找数组中前三名
def find_top3(arr):
    if arr is None or len(arr) < 3:
        print("参数不合法")
        return 
    
    r1 = r2 = r3 = -2 ** 31
    i = 0
    while i < len(arr):
        if arr[i] > r1:
            r3 = r2
            r2 = r1
            r1 = arr[i]
        elif arr[i] > r2 and arr[i] != r1:
            r3 = r2
            r2 = arr[i]
        elif arr[i] > r3 and arr[i] != r2:
            r3 = arr[i]

        i += 1

    print("前三名为：",r1,r2,r3)


if __name__ == "__main__":
    arr = [4,7,1,2,3,5,3,6,3,2]
    find_top3(arr)
