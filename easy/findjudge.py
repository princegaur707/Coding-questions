class Solution:
    def findJudge(self, N, trust):
        arr=arr1=arr2=set()
        for num in trust:
            print(num)
            arr.add(num[0])
            arr1.add(num[1])
        print(arr)
        print(arr1)
        for i in range(1,N):
            if i not in arr:
                for key,value in trust:
                    if value==i:
                        arr2.add(key)
                if(len(arr2)==N-1):
                    return i
                else:
                    return -1
obj=Solution()
print(obj.findJudge(3,[[1,2],[2,3]]))