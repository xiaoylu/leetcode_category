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

Dynamic Programming view:
* Sort the works by their qualities
* The optimal `K` workers in the first `i-1` workers are known
* If the `i`-th worker joins, then we must replace the worker with highest ratio in the first `i-1` workers; Otherwise, both the sum of quality and highest ratio would increase as `i`-th worker joins.

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

## Two queues for medium
**LC 295. Find Median from Data Stream**

Design a data structure that supports the following two operations:

* `void addNum(int num)` - Add a integer number from the data stream to the data structure.
* `double findMedian()` - Return the median of all elements so far.

```
    def addNum(self, num):
        # the size of hi queue is equal to or one more than the size of lo queue
        # len(self.hi) == len(self.lo)
        # or len(self.hi) == len(self.lo) + 1
        if not self.hi:
            heappush(self.hi, num)
        elif num >= self.hi[0]:
            heappush(self.hi, num)
            if len(self.hi) > len(self.lo) + 1:
                heappush(self.lo, -heappop(self.hi))
        else:
            heappush(self.lo, -num)
            if len(self.hi) < len(self.lo):
                heappush(self.hi, -heappop(self.lo))
```

**LC 480. Sliding Window Median**

See
<https://leetcode.com/problems/sliding-window-median/discuss/96347/O(n*log(n))-Time-C++-Solution-Using-Two-Heaps-and-a-Hash-Table>

Insert the i-th element (try self.hi first, if fails, then try self.lo)
Remove the (i-k)-th element (try self.hi first, if fails, then try self.lo)

Then the size of **effective** elements in two queues can only differ by 0 or 2. 
* If differ by 2, move one element from one queue to the other
* If differ by 0, do nothing.

Before you re-balance two heaps, make sure at the top of a heap is an effective element.
Before you compute the median, make sure both tops are effective elements.

```
from heapq import heappush, heappop
class Solution:
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        if not nums or k > len(nums) or k == 0: return []
        
        def clean(lo, hi, count):
            while lo and count[-lo[0]] > 0:  count[-lo[0]] -= 1; heappop(lo)
            while hi and count[hi[0]] > 0: count[hi[0]] -= 1; heappop(hi)
                    
        lo, hi = [], []
        count = collections.defaultdict(int)
        
        for i in range(k): heappush(hi, nums[i])
        for _ in range(k//2): heappush(lo, -heappop(hi))
            
        # now we have len(h) >= len(l)
        res = []
        for i in range(k, len(nums)):
                
            if k & 1: res.append(float(hi[0]))
            else: res.append((hi[0] - lo[0]) / 2.)
            
            balance = 0
            
            # push the current element
            if nums[i] >= hi[0]: balance += 1; heappush(hi, nums[i])
            else: balance -= 1; heappush(lo, -nums[i])
                
            # pop the element k steps before
            if nums[i-k] >= hi[0]:
                balance -= 1
                if nums[i-k] == hi[0]: heappop(hi)
                else: count[nums[i-k]] += 1
            else:
                balance += 1
                if nums[i-k] == -lo[0]: heappop(lo)
                else: count[nums[i-k]] += 1
                    
            clean(lo, hi, count)
            
            # at the top of hi/lo must be an effective element??
            if balance > 0: heappush(lo, -heappop(hi))
            elif balance < 0: heappush(hi, -heappop(lo))
            
            clean(lo, hi, count)
                
        if k & 1: res.append(float(hi[0]))
        else: res.append((hi[0] - lo[0]) / 2.0)
                
        return res
```

## Lazy deletion

Python heapq does not support removal, you can do lazy deletion which removes a element only when it's at the top. Specifically,
* Use a hash table to count the number of removals of each element
* When such element emerges to the top of a queue, remove it, decrease the count of removal until zero

**LC 716. Max Stack**
```
```


