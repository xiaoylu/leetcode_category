class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictMap = {}
        for idx, val in enumerate(nums):
            if target - val in dictMap:
                return dictMap[target-val], idx
            dictMap[val] = idx
