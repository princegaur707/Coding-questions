class Solution:
    def isPalindrome(self, s):
        string=""
        for i in s:
            if i.isalnum():
                string+=i.lower()
        string=string.replace(" ","")       
        return string==string[::-1]
obj=Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))
print(obj.isPalindrome("race a car"))
print(obj.isPalindrome("0P"))
        