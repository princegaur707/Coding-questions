nums=[1,2,3,4]
cnt=1
l=len(nums)
arr=[]
for i in range(1,l):
    if(nums[i-1]<nums[i]):
        cnt+=1
        i+=1
    else:
        arr.append(cnt)
        i+=1
if(l==1):
    print("1")
elif(len(arr)>0):
    print(max(arr))
else:
    print("0")