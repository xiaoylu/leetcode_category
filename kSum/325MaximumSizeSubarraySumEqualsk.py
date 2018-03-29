class Solution:
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        acc = 0
        ret = 0
        loc = {0:-1}
        for idx, val in enumerate(nums):
            acc += val
            if acc not in loc:
                loc[acc] = idx
            if acc-k in loc:
                ret = max(ret, idx-loc[acc-k])
        return ret
