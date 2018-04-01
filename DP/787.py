import collections
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = collections.defaultdict(dict)
        for i,j,w in flights:
            graph[i][j] = w
        heap = [(0,src,K+1)]
        while heap:
            price,i,k = heapq.heappop(heap)
            if (i==dst):
                return price
            if k>0:
                for j in graph[i]:
                    heapq.heappush(heap, (price+graph[i][j],j,k-1))
        return -1
