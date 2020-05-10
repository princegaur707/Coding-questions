class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        arr=[]
        nums=Counter(nums)
        for key,value in nums.items():
            if value==2:
                arr.append(key)
        return arr