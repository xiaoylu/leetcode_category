# Priority Queue

## Sort + Priortiy Queue

**LC 857. Minimum Cost to Hire K Workers**

There are N workers.  The i-th worker has a `quality[i]` and a minimum wage expectation `wage[i]`.

Now we want to hire exactly K workers to form a paid group.  When hiring a group of K workers, we must pay them according to the following rules:

* Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
* Every worker in the paid group must be paid at least their minimum wage expectation.

Return the least amount of money needed to form a paid group satisfying the above conditions.

We compute the ratio of money/quality for every worker. Given a group, the maximum money/quality ratio should be paid.

So the least amount of money would be `max(r1, r2, .. rk) * sum(r1, r2, .. rk)`. Note that if we already have `K` workers with the smallest sum of quality, the only way to save money is to replace the worker with highest pay. 

```
    def mincostToHireWorkers(self, quality, wage, K):
        # q 10 20  5
        # r 7  2.5 6
        #   5 10 20  30
        #   6 7  2.5 99 
        # max(r) * sum(q)
        # start with smallest sum(q), 
        # we have to increase sum(q) while reducing max(r)
        
        if not quality or K==0: return 0
        
        rate = []
        for q, w in zip(quality, wage):
            rate.append(w/q)
        A = sorted((q, r) for q, r in zip(quality, rate))
        
        hp = [(-r, q) for q, r in A[:K]]
        heapq.heapify(hp)
        sumq, maxr = sum(q for q, r in A[:K]), max(r for q, r in A[:K])
        
        res = sumq * maxr
        for q, r in A[K:]:
            _R, Q = heapq.heappop(hp)
            heapq.heappush(hp, (-r, q))
            
            sumq = sumq - Q + q
            maxr = -hp[0][0]
            res = min(res, sumq * maxr)
        return res
```
