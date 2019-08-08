# 如何求数组连续最大和及其位置
class Test():
    def __init__(self):
        self.begin = 0
        self.end = 0
    
    def getBegin(self):
        return self.begin
    
    def getEnd(self):
        return self.end
    

    def maxSubArray(self,arr):
        n = len(arr)
        maxSum = -2 ** 32
        nSum = 0
        nStart = 0
        i = 0

        while i < n:
            if nSum < 0:
                nSum = arr[i]
                nStart = i
            else:
                nSum += arr[i]
            
            if nSum > maxSum:
                maxSum = nSum
                self.begin = nStart
                self.end = i
            i += 1
        return maxSum
        

if __name__ == "__main__":
    t = Test()
    arr = [1,-2,4,8,-4,7,-1,-5]
    print("连续最大和为：", t.maxSubArray(arr))
    result = "开始位置为{}，终止位置为{}".format(t.getBegin(),t.getEnd())
    print(result)
