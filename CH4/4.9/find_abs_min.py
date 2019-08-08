# 如何求数组中绝对值最小的数
# 顺序比较法
def finMin(array):
    if array is None or len(array) <=0 :
        print("参数不合理")
        return 
    
    mins = 2 ** 32
    i = 0
    while i < len(array):
        if abs(array[i]) < abs(mins):
            mins = array[i]
        i += 1

    return mins


if __name__ == "__main__":
    arr = [-10,-5,-2,7,15,20]
    print("绝对值最小的元素为",finMin(arr))
