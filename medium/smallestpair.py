class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pair = []
        m = len(nums1)
        n = len(nums2)
        heap = []
        
        def push(i, j):
            if 0 <= i <m and 0 <= j < n:
                heapq.heappush(heap, (nums1[i]+nums2[j], i, j))
            return
        
        push(0, 0)
        while heap and len(pair) < k:
            _, i, j = heapq.heappop(heap)
            pair.append([nums1[i], nums2[j]])
            push(i, j+1)
            if j == 0:
                push(i+1, 0)
        
        return pair