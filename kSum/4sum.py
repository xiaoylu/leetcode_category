import itertools
from collections import defaultdict
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        two_sum = defaultdict(list)
        ret = set()
        for (idx1, val1), (idx2, val2) in itertools.combinations(enumerate(nums), 2):
            two_sum[val1+val2].append({idx1,idx2})
        keys = two_sum.keys()
        for sum2 in list(keys):
            if sum2 in two_sum and target-sum2 in two_sum:
                for pair1 in two_sum[sum2]:
                    for pair2 in two_sum[target-sum2]:
                        if pair1.isdisjoint(pair2):
                            ret.add(tuple(sorted([nums[i] for i in pair1|pair2])))
                del two_sum[sum2]
                two_sum.pop(target-sum2, None)
        return [list(i) for i in ret]
