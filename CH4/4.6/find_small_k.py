# 如何找出数组中第k小的数
# 类快速排序方法
def find_small_K(array,low,high,k):
    i = low
    j = high
    splitElem = array[i]
    while i < j:
        while i < j and array[j] >= splitElem:
            j -= 1
        if i < j:
            array[i] = array[j]
            i += 1
        while i < j and array[i] < splitElem:
            i += 1
        if i < j:
            array[j] = array[i]
            j -= 1

    array[i] = splitElem
    subArrayIndex = i - low
    if subArrayIndex == k-1:
        return array[i]
    elif subArrayIndex > k-1:
        return find_small_K(array,low,i-1,k)
    else:
        return find_small_K(array,i+1,high,k-(i-low)-1)


if __name__ == "__main__":
    k = 3
    array = [4,0,1,0,2,3]
    print(find_small_K(array,0,len(array)-1,k))
    