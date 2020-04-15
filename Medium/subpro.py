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
