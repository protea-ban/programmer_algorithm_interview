# 如何找到数组中唯一的重复元素
# 空间换时间法 哈希法
def findDup(array):
    if array is None:
        return -1

    lens = len(array)
    hashTable = dict()
    i = 0
    while i < lens - 1:
        hashTable[i] = 0
        i += 1
    j = 0
    while j < lens:
        if hashTable[array[j] - 1] == 0:
            hashTable[array[j] - 1] += 1
        else:
            return array[i]

        j += 1

    return -1


if __name__ == '__main__':
    array = [1,3,4,2,5,3]
    print(findDup(array))
