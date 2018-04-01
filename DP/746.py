class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        mc = [0]*(len(cost)+1)
        for i in range(2,len(cost)+1):
            mc[i] = min(mc[i-1]+cost[i-1],mc[i-2]+cost[i-2])
        return mc[len(cost)]
