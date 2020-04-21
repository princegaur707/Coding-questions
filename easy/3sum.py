import bisect
class Solution:
    def threeSum(self, nums):
        ref = {}
        for i in nums:
            if i not in ref:
                ref[i] = 1
            else:
                ref[i] += 1
        nums=sorted(ref)
        print("1",ref)        
        ans=[]
        for i, itemI in enumerate(nums):
            if itemI == 0:
                if ref[itemI] > 2:
                    ans.append((0, 0, 0))
            else:
                if ref[itemI] > 1 and -2 * itemI in ref:
                    ans.append((itemI, itemI, -2 * itemI))
            if itemI < 0:
                target = -itemI
                left = bisect.bisect_left(nums, target-nums[-1], i+1)
                right = bisect.bisect_right(nums, target // 2, left)
                for itemJ in nums[left : right]:
                    itemK = target - itemJ
                    if itemK in ref and itemK != itemJ:
                        ans.append((itemI, itemJ, itemK))
        return ans
obj=Solution()
print(obj.threeSum([-1, 0, 1, 2, -1, -4]))