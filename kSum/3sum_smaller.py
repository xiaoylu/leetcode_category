class Solution:
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ret = 0
        i = 0
        nums.sort()
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i]+nums[j]+nums[k] < target:
                    ret += (k-j)
                    j += 1
                else:
                    k -= 1
            i += 1
        return ret
