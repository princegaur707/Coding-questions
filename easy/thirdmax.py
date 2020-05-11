class Solution(object):
    def thirdMax(self, nums):
        v = [float('-inf'), float('-inf'), float('-inf')]
        for num in nums:
            print("num",num)
            if num not in v:
                if num > v[0]:   v = [num, v[0], v[1]] print('v',v)
                elif num > v[1]: v = [v[0], num, v[1]] print('v',v)
                elif num > v[2]: v = [v[0], v[1], num] print('v',v)
        return max(nums) if float('-inf') in v else v[2]
obj=Solution()
print(thirdMax([2,2,3,1]))