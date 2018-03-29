# 80. Remove Duplicates from Sorted Array II
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        for n in enumerate(nums):
            if j < 2 or n > nums[j-2]:
                nums[j] = n
                j += 1
        return j
