class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        ret = [1]*len(ratings)
        for i in range(1,len(ratings),1):
            ret[i] = ret[i-1] + 1 if ratings[i] > ratings[i-1] else 1
        rbase = 1
        for j in range(len(ratings)-2,-1,-1):
            rbase = rbase + 1 if ratings[j] > ratings[j+1] else 1
            ret[j] = max(rbase, ret[j])
        return sum(ret)
