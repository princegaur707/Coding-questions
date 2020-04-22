import bisect
class Solution:
    def threeSum(self, nums):
        ref = {}
        for i in nums:
            if i not in ref:
                ref[i] = 1
            else:
                ref[i] += 1
        nums.sort()
        print(nums)
        nums=sorted(ref)
        print("1",ref)    
        print("2",nums)    
        ans=[]
        for i, itemI in enumerate(nums):
            print("i,itemI:  ",i,itemI)
            if itemI == 0:
                print("1st if")
                if ref[itemI] > 2:
                    ans.append((0, 0, 0))
                print(ans)
            else:
                print("1st else")
                if ref[itemI] > 1 and -2 * itemI in ref:
                    ans.append((itemI, itemI, -2 * itemI))
                print(ans)
            if itemI < 0:
                print("2nd if")
                target = -itemI
                print("target:  ",target)
                left = bisect.bisect_left(nums, target-nums[-1], i+1)
                print("Left:   ",left, end=" ")
                right = bisect.bisect_right(nums, target // 2, left)
                print("Right:  ",right)
                for itemJ in nums[left : right]:
                    print("itemJ:  ",itemJ)
                    itemK = target - itemJ
                    if itemK in ref and itemK != itemJ:
                        ans.append((itemI, itemJ, itemK))
                print(ans)
        return ans
obj=Solution()
print(obj.threeSum([-1, 0, 1, 2, -1, -4]))