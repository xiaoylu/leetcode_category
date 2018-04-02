class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = collections.Counter(nums)
        prev, cur = 0, 0
        for v in range(10001):
            prev, cur = cur, max(prev+cnt[v]*v,cur)
        return cur
