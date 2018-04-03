from heapq import heapreplace, heappush
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h = []
        for n in nums:
            if len(h)<k:
                heappush(h,n)
            elif n>h[0]:
                heapreplace(h,n)
        return h[0]
