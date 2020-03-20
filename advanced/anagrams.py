#replace anagrams from list of anagrams
strs=["eat", "tea", "tan", "ate", "nat", "bat"]
main=[]
list1=[]
for i in range(len(strs)):
    list1=[]
    list1.append(strs[i])
    string1=list(strs[i])
    string1.sort()
    for j in range(i+1,len(strs)):
        string2=list(strs[j])
        string2.sort()
        if(string1==string2):
            list1.append(strs[j])
        j+=1
    i+=1
    main.append(list1)
print(main)
