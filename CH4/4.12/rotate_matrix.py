# 对数组旋转，逆时针旋转45度
# 思路：从右上角对数组中的元素进行输出
def rotateArr(arr):
    lens = len(arr)
    # 打印二维数组的右上半部分
    i = lens - 1
    while i > 0:
        row = 0
        col = i
        while col < lens:
            print(arr[row][col], end=' ')
            row += 1
            col += 1
        print()
        i -= 1
    # 打印左下半部分
    i = 0
    while i < lens:
        row = i
        col = 0
        while row < lens:
            print(arr[row][col], end=' ')
            row += 1
            col += 1
        print()
        i += 1


if __name__ == "__main__":
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    rotateArr(arr)
        