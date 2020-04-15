#https://leetcode.com/problems/maximum-product-subarray/
class Solution:
    def maxProduct(self, A):
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        print(A)
        print(B)
        return max(A + B)
obj=Solution()
print(obj.maxProduct([1,2,-4,1]))

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        i = 0
        currentMax, currentMin, ans = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            tmp = currentMax
            currentMax = max(n, n*currentMax, n*currentMin)
            currentMin = min(n, n*tmp, n*currentMin)
            ans = max(ans, currentMax)
        return ans
            
