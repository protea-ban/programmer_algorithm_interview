# 如何求集合的所有子集
# 位图法
def get_all_sub_set(array, mask, c):
    length = len(array)
    if length == c:
        print("{", end=' ')
        i = 0
        while i < length:
            if mask[i] == 1:
                print(array[i], end=' ')
            i += 1
        print("}")
    else:
        mask[c] = 1
        get_all_sub_set(array,mask,c+1)
        mask[c] = 0
        get_all_sub_set(array, mask, c+1)


if __name__ == "__main__":
    array = ['a', 'b', 'c']
    mask= [0,0,0]
    get_all_sub_set(array, mask, 0)