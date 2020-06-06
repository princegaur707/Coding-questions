def finddisappeared(nums):
    for num in nums:
        index=abs(num)-1
        nums[index]=-abs(nums[index])
    print([i for i,num in enumerate(nums,1) if num>0])

finddisappeared([4,3,2,7,8,2,3,1])