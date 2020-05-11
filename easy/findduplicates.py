#https://leetcode.com/problems/find-all-duplicates-in-an-array/
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        arr=[]
        nums=Counter(nums)
        for key,value in nums.items():
            if value==2:
                arr.append(key)
        return arr
obj=Solution()
print(obj.findDuplicates([4,3,2,7,8,2,3,1]))
