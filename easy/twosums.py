#https://leetcode.com/problems/two-sum/
#Find two numbers who sum is equal to target
class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            print("i,j: ",i,n)
            print("d: ",d)
            try:
                return [d[target - n], i]
            except:
                d[n] = i
            print(d.items())
obj=Solution()
print(obj.twoSum([3,3],6))
