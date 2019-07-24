# 如何从数组中找出满足a+b=c+d的两个数对
# 用来存储数对
class Pair():
    def __init__(self, first, second):
        self.first = first
        self.second = second


def findPairs(arr):
    sumPair = dict()
    n = len(arr)
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            sums = arr[i] + arr[j]
            if sums not in sumPair:
                pair = Pair(arr[i], arr[j])
                sumPair[sums] = pair
            else:
                p = sumPair[sums]
                res = "{}+{}={}+{}".format(arr[i],arr[j],p.first,p.second)
                print(res)
                return True
            j += 1
        i += 1
        
    return False


if __name__ == '__main__':
    arr = [3,4,7,10,20,9,8]
    findPairs(arr)
