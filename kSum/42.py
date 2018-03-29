class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1: return 0
        cap = [0]*len(height)
        ret = 0
        curmax = height[0]
        for i,n in enumerate(height):
            curmax = max(curmax, n)
            cap[i] = curmax
        curmax = height[-1]
        for j,n in reversed(list(enumerate(height))):
            curmax = max(curmax, n)
            ret += min(cap[j],curmax)-n
        return ret
