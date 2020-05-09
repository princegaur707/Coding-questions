class Solution:
    def findMaxLength(self, nums):
        d = {0: -1}    # Considering nothing at -1 position instead of index and starting indexing from 1
        key, maxL = 0, 0
        for i in range(len(nums)):
            print("i,key:   ",i,key)
            key += nums[i] or -1
            if key not in d:
                print("If")
                d[key] = i
            else:
                print("Else")
                maxL = max(maxL, i-d[key])
            print("i,key,maxL: ",i,key,maxL)
            print("d:  ",d)
            print("_____________________________________________________________________________")
        return maxL
obj=Solution()
print(obj.findMaxLength([0, 0, 1, 0, 0, 0, 1, 1]))