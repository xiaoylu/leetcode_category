from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        out = []
        d = deque()
        if k==0: return []
        for i,n in enumerate(nums):
            while d and nums[d[-1]]<n:
                d.pop()
            d += i,
            if d[0]==i-k:
                d.popleft()
            if i>=k-1:
                out.append(nums[d[0]])
        return out
