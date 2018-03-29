#26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<1: return 0
        i = 1
        prev = nums[0]
        for j in range(len(nums)):
            if nums[j] != prev:
                nums[i] = nums[j]
                i += 1
            prev = nums[j]
        return i

