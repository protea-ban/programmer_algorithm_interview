# 如何找到数组中出现奇数次的数
# 字典法
def get2num(arr):
    if arr is None or len(arr) < 1:
        print("参数错误")
        return

    dic = dict()
    i = 0
    while i < len(arr):
        if arr[i] not in dic:
            dic[arr[i]] = 1
        else:
            dic[arr[i]] = 0

        i += 1

    for k,v in dic.items():
        if v == 1:
            print(k)


if __name__ == "__main__":
    arr = [3,5,6,6,5,7,2,2]
    get2num(arr)
    