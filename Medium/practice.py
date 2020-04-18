#Find two numbers who sum is equal to target
class Solution:
    def twoSum(self, nums, target):
        dict1={}
        for i in range(len(nums)):
            dict1[i]=nums[i]
        dict1={value:key for key,value in dict1.items()}
        print(dict1)
        for key,value in dict1.items():
            try:
                return [dict1[target - key], value]
            except:
                dict1[n] = i
obj=Solution()
print(obj.twoSum([2,7,8,9],9))
