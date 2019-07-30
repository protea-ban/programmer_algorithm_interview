def findDup(array):
    if array is None:
        return -1

    lens = len(array)
    index = 0
    i = 0
    while True:
        if array[i] >= lens:
            return -1

        if array[index] < 0:
            break

        array[index] *= -1
        index = -1*array[index]
        if index >= lens:
            return -1

    return index


if __name__ == '__main__':
    array = [1,3,4,2,5,3]
    print(findDup(array))
