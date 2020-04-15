#https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums):
        currentMax, currentMin, ans =ans1 = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            tmp = currentMax
            currentMax = max(n, n*currentMax, n*currentMin) 
            currentMin = min(n, n*tmp, n*currentMin) # It is required as in case of [-2,3,-4] at last iteration it will yiled 24 and others -4,-12 
            ans = max(ans, currentMax)
            ans1= min(ans,currentMin)
            print(f"n: {n} tmp: {tmp} MAX:{currentMax} MIN: {currentMin} Ans:{ans} Ans1:{ans1}")
        return [ans,ans1]
obj=Solution()
print(obj.maxProduct([-2,3,-4]))          
 