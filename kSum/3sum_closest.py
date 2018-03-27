class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ret = sum(nums[0:3])
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if abs(nums[i]+nums[j]+nums[k]-target)<abs(ret-target): ret = nums[i]+nums[j]+nums[k]
                elif nums[i]+nums[j]+nums[k]>target: k-=1
                elif nums[i]+nums[j]+nums[k]<target: j+=1
                else : return target
            i += 1
        return ret
