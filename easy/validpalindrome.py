class Solution:
    def isPalindrome(self, s):
        string=""
        for i in s:
            if i.isalpha():
                string.join(i)
                print(string)
        string=string.replace(" ","")        
        string=string.lower()
        return s==s[::-1]
        