# 异或法 相同元素异或为0 0与其他元素异或为元素本身
def findDup(array):
    if array is None:
        return -1

    lens = len(array)
    result = 0
    i= 0
    while i < lens:
        result ^= array[i]
        i += 1

    j = 1
    while j < lens:
        result ^= j
        j += 1

    return result


if __name__ == '__main__':
    array = [1,3,4,2,5,3]
    print(findDup(array))
