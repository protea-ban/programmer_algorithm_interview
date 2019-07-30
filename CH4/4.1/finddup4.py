def findDup(array):
    if array is None:
        return -1

    slow = 0
    fast = 0

    while True:
        fast = array[array[fast]]
        slow = array[slow]
        if slow == fast:
            break

    fast = 0
    while True:
        fast = array[fast]
        slow = array[slow]
        if slow == fast:
            return slow


if __name__ == '__main__':
    array = [1,3,4,2,5,3]
    print(findDup(array))
