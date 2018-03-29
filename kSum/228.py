class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums)<1: return []
        j = 0
        ret = []
        for i in range(1,len(nums)+1):
            if i==len(nums) or nums[i] != nums[i-1]+1:
                ret.append( "%d" %nums[j] if i-1==j else "%d->%d" % (nums[j], nums[i-1]) )
                j = i
        return ret

class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ret, r = [], []
        for n in nums:
            if n-1 not in r:
                r = []
                ret.append(r)
            r[1:] = n,
        return ['->'.join(map(str, r)) for r in ret]
