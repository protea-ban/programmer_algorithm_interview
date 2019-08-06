# 查找数组中元素的最大值和最小值
# 分治法变形
class MaxMin():
    def getMaxMin(self,array,l,r):
        if array is None:
            print("参数错误")
            return

        list = []
        m = (l+r) // 2
        if l == r:
            list.append(array[l])
            list.append(array[l])
            return list

        if l + 1 == r:
            if array[l] >= array[r]:
                max = array[l]
                min = array[r]
            else:
                max = array[r]
                min = array[l]
            list.append(min)
            list.append(max)
            return list

        lList = self.getMaxMin(array,l,m)
        rList = self.getMaxMin(array, m+1, r)
        max = lList[1] if lList[1] > rList[1] else rList[1]
        min = lList[0] if lList[0] < rList[0] else rList[0]
        list.append(min)
        list.append(max)

        return list


if __name__ == '__main__':
    arr = [7,3,19,40,4,7,1]
    m = MaxMin()
    result = m.getMaxMin(arr,0,len(arr)-1)
    print("max=", result[1])
    print("min=", result[0])
