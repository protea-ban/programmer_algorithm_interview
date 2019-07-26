# 如何判断一个数组是否是二元查找树后序遍历的序列
def IsAfterOrder(arr, start, end):
    if arr is None:
        return False

    # 后序遍历的最后一个元素是根结点
    root = arr[end]
    i = start
    # 找到第一个大于root的值，其前面都是左子树
    while i < end:
        if arr[i] > root:
            break
        i += 1

    # 因为后序，所以从i开始之后的结点值都大于root
    j = i
    while j < end:
        if arr[j] < root:
            return False
        j += 1

    left_IsAfterOrder = True
    right_IsAfterOrder = True

    # 判断小于root值的序列是否为后序遍历
    if i > start:
        left_IsAfterOrder = IsAfterOrder(arr, start, i-1)

    # 判断大于root值的序列是否为后序遍历
    if j < end:
        right_IsAfterOrder = IsAfterOrder(arr, i, end)

    return left_IsAfterOrder and right_IsAfterOrder


if __name__ == '__main__':
    arr = [1,3,2,5,7,6,4]
    result = IsAfterOrder(arr,0,len(arr)-1)
    i = 0
    if result:
        print("是")
    else:
        print("不是")
