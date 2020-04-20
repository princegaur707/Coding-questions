def almostIncreasingSequence(str1):
    arr1 = str1
    arr1.remove(max(arr1))
    cnt=cnt1=1
    for i in range (1, len(arr1)):
        if(arr1[i-1]<arr1[i]):
            pass
        else:
            cnt-=1
    str1.remove(min(str1))
    for i in range (1,len(str1)):
        if(str1[i-1]<str1[i]):
            pass
        else:
            cnt1-=1
    if(cnt==1 or cnt1==1):
        return True
    else:
        return False
while True:
    print(almostIncreasingSequence([1, 2, 1, 2]))