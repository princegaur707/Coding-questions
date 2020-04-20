#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#find minimum of array obtained after rotating from certain point
class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums)-1   
        while left < right:
            print(left,right)
            mid = (left + right) // 2           
            if nums[mid] > nums[right]: # If mid one is greater implies smallest will be in the right side of it
                left = mid + 1
            else:  
                right = mid
            print("MID:",mid)
        return nums[left]
obj=Solution()
print(obj.findMin([3,4,5,6,1,2]))