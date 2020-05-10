#https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# For each number i in nums,
# we mark the number that i points as negative.
# Then we filter the list, get all the indexes
# who points to a positive number
def findDisappearedNumbers(nums):
    for num in nums:
        index = abs(num) - 1
        nums[index] = -abs(nums[index])
        print("num,index,nums[index]",num,index,nums[index])
        print("nums:",nums)
    return [i for i, num in enumerate(nums,1) if num > 0]
print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
