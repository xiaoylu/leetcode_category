class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1 and nums[0]<s: return 0
        cur = 0
        i = 0
        min_l = len(nums)+1
        for j, val in enumerate(nums):
            cur += val
            while i <= j and cur >= s:
                min_l = min(min_l, j-i+1)
                cur -= nums[i]
                i += 1
        return min_l if min_l <= len(nums) else 0
