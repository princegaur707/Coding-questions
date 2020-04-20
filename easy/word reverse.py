#Input: "Let's take LeetCode contest"
#Output: "s'teL ekat edoCteeL tsetnoc"
s="  Let's take LeetCode contest  "
print(s)
s=s.strip()
print(s)
s=s.split()
print(s)
arr=[]
str1=" "
for word in s:
    word=word[::-1]
    arr.append(word)
str1=str1.join(arr)
s=str1
print(str1)
print(s)
