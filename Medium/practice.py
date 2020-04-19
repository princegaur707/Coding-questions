#Find two numbers who sum is equal to target
class Solution:
    def twoSum(self, nums, target):
        dict1={}
        for i in range(len(nums)):
            dict1[i]=nums[i]
        print("1",dict1)
        dict1={value:key for key,value in dict1.items()}
        print("2",dict1)
        for key,value in dict1.items():
            try:
                return [dict1[target - key], value]
            except:
                dict1[n] = i
obj=Solution()
print(obj.twoSum([3,3],6))
