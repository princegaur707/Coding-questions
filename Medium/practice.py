#Find two numbers who sum is equal to target
class Solution:
    def twoSum(self, nums, target):
        dict1 = {}
        dict1={value:key for key,value in dict1.items()}
        for key,value in dict1:
            try:
                return [dict1[target - n], i]
            except:
                dict1[n] = i
obj=Solution()
print(obj.twoSum([2,7,8,9],9))
