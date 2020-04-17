#Find two numbers who sum is equal to target
class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            try:
                return [d[target - n], i]
            except:
                d[n] = i
obj=Solution()
print(obj.twoSum([2,7,8,9],9))