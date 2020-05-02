# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        left=1
        right=n
        mid=(left+right)//2
        while left<right:
            if isBadVersion(mid)==True and isBadVersion()==False:
                return mid
            if isBadVersion(mid):
                right=mid-1
            else:
                left=mid+1

class Solution:
    def firstBadVersion(self, n):
        low = 1
        high = n
        
        while low < high:
            mid = low+(high-low)//2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid+1
        return low

class Solution:
    def firstBadVersion(self, n):
        class Wrap:
            def __getitem__(self, i):
                return isBadVersion(i)
        return bisect.bisect(Wrap(), False, 0, n)# finding where we can keep the false at the righmost possible place
        #bisect(list, num, beg, end)