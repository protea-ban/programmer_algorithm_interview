# 一数组，每行都按照从左到右递增排序，每列都按照从上到下递增排序，判断数组中是否含一个整数
def find_with_binary(array,data):
    if array is None:
        return False
    i = 0
    rows = len(array)
    columns = len(array[0])
    j = columns - 1
    while i < rows and j >= 0:
        if array[i][j] == data:
            return True
        elif array[i][j] > data:
            j -= 1
        else:
            i += 1
        
    return False


if __name__ == "__main__":
    array = [
        [0,1,2,3,4],
        [10,11,12,13,14],
        [20,21,22,23,24],
        [30,31,32,33,34],
        [40,41,42,43,44]
    ]
    print(find_with_binary(array, 17))
    print(find_with_binary(array, 31))