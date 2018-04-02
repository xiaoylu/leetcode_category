class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev, cur = 0, 0
        for n in nums:
            prev, cur = cur, max(prev+n, cur)
        return cur
