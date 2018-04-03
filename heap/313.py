#class Solution:
#    def nthSuperUglyNumber(self, n, primes):
#        """
#        :type n: int
#        :type primes: List[int]
#        :rtype: int
#        """
#        ug = [1]
#        def gen(prime):
#            for u in ug:
#                yield u*prime
#        h = heapq.merge(*map(gen, primes))
#        while len(ug)<n:
#            u = next(h)
#            if u != ug[-1]:
#                ug.append(u)
#        return ug[-1]
#
from heapq import heappush,heappop,heapify
class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ug = [1]
        idx = {p:0 for p in primes}
        while len(ug)<n:
            tmp = [(p*ug[idx[p]],p) for p in primes]
            heapify(tmp)
            m = tmp[0][0]
            while tmp and m == tmp[0][0]:
                idx[tmp[0][1]] += 1
                heappop(tmp)
            ug.append(m)
        return ug[-1]
