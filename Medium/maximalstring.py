# checking effectiveness of maximal string : for ex- aaaaabbbccc-a5b3c3
t=int(input())
while(t>0):
    s=input(
    str2=""
    cnt=1
    l1=len(s)
    str2=str2+s[0]
    for i in range(1,l1):
        if(s[i-1]==s[i]):
            cnt+=1
        else:
            
            if(cnt>0):
                str2=str2+str(cnt)
                cnt=1
            str2=str2+s[i]
    str2=str2+str(cnt)     
    l2=len(str2)
    if(l1>l2):
        print("YES")
    else:
        print("NO")
    t=t-1
