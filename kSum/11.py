class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        ret = 0
        while i<j:
            if height[i]<height[j]:
                area = (j-i)*height[i]
                i += 1
            else:
                area = (j-i)*height[j]
                j -= 1
            ret = max(ret, area)
        return ret
