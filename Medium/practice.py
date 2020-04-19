class Solution:
    def findClosestElements(self, arr, k, x):
        left, right = 0, len(arr) - k
        while left < right:
            print("Left,Right:   ",left,right)
            mid = (left+right)//2
            print("Mid:   ",mid)
            if x - arr[mid] > arr[mid + k] - x:
                print(x-arr[mid])
                print(arr[mid+k]-x)
                print("IF")
                left = mid + 1
            else:
                print("Else")
                right = mid
        return arr[left:left + k]
obj=Solution()
print(obj.findClosestElements([1,2,3,4,6,7,8,9,10],4,9))
