from collections import Counter
def threesums(nums):
    ref=Counter(nums)
    print(ref)
    ans=[]
    nums.sort()
    for i,itemI in enumerate(nums):
        if itemI==0:
            if ref[itemI]>2:
                ans.append([0,0,0])
        else:
            if ref[itemI]>2 and -2*itemI>0:
                ans.append([itemI,itemI,-2*itemI])
        if




threesums([-1, 0, 1, 2, -1, -4])
        