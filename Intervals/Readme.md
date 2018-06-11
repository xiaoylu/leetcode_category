## Intervals
Many problems involve intervals.

LC 253. Meeting Rooms II. 
Given an array of meeting time intervals, find the minimum number of conference rooms required.
The greedy solution which puts the next earliest meeting in ANY available time line (every room has a time line). 
But here we choose the time line with the earliest ending time because it take O(log n) time to check by heap.
```
    def minMeetingRooms(self, intervals):
        count, hp = 0, []
        for s, e in sorted((v.start, v.end) for v in intervals):
            if hp and hp[0] <= s:
                heapq.heappop(hp)
            else:
                count += 1
            heapq.heappush(hp, e)
        return count
```

While the first operation is very common, another important technic is "Discretization". 
We record the independent "time slots" formed by all the starts and ends. (Not necessarily the ends are after starts)
Get a `count` array for each slot, when an interval comes in, add `count[i]` for all slot `i` inside this interval.
You will know the maximum number of one slot occupied by the intervals. This number is the result.

LC 253. Meeting Rooms II. 
```
    def minMeetingRooms(self, intervals):
        ts = set(t for v in intervals for t in [v.start, v.end])
        index = {t:i for i, t in enumerate(sorted(ts))}
        count = [0] * len(ts)
        for v in intervals:
            for i in range(index[v.start], index[v.end]):
                count[i] += 1
        return max(count or [0])
```

The solution above may take `O(n^2)` time. Can we skip the second loop visiting all slots inside an interval?
Segment Tree with lazy propagation can operate on a "range" in `O(log n)` time. Yet, it is too complicated.

A simpler way is to sort all the starts and ends together, WITH a signal indicating the distinction.
```
    def minMeetingRooms(self, intervals):
        ret, count = 0, 0
        for t, sig in sorted(ss for s in intervals for ss in [(s.start, 1), (s.end, -1)]):
            count += sig
            ret = max(ret, count)
        return ret
```

Let's try a more complicated problem.


