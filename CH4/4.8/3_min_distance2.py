# 如何求解最小三元组距离
# 最小距离法 
def maxs(a,b,c):
    maxs = b if a < b else a
    maxs = c if maxs < c else maxs
    return maxs

def mins(a,b,c):
    mins = b if a > b else a
    mins = c if mins > c else mins
    return mins

def minDistance(a,b,c):
    aLen = len(a)
    bLen = len(b)
    cLen = len(c)
    curDist = 0
    minsd = 0
    minDist = 2**32
    i = 0
    j = 0
    k = 0

    while True:
        curDist = maxs(abs(a[i]-b[j]),abs(a[i]-c[k]),abs(b[j]-c[k]))
        if curDist < minDist:
            minDist = curDist
        # 找到当前遍历三个数组中最小的
        minsd = mins(a[i],b[j],c[k])
        if minsd == a[i]:
            i += 1
            if i >= aLen:
                break
        elif minsd == b[j]:
            j += 1
            if j >= bLen:
                break
        else:
            k += 1
            if k >= cLen:
                break
    
    return minDist


if __name__ == "__main__":
    a = [3,4,5,7,15]
    b = [10,12,14,16,17]
    c = [20,21,23,24,37,40]
    print("最小距离为：", minDistance(a,b,c))