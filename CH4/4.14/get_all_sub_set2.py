# 如何求集合的所有子集
# 迭代法
def get_all_sub_set(str):
    if str is None or len(str) < 1:
        print("参数不合理")
        return None
    arr = []
    arr.append(str[0:1])
    i= 1
    while i < len(str):
        lens = len(arr)
        j = 0
        while j < lens:
            arr.append(arr[j]+str[i])
            j += 1
        arr.append(str[i:i+1])
        i += 1
    return arr


if __name__ == "__main__":
    result = get_all_sub_set("abc")
    i = 0
    while i < len(result):
        print(result[i])
        i += 1
        