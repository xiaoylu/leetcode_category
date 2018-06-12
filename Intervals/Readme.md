## Intervals
Many problems involve intervals. **Discretization** is usually a good choice dealing with intervals.

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

LC 218. The Skyline Problem. The skyline is the outer contour of building roofs.
We discretize the left and right walls of buildings, so just 
```
        xs = sorted(set(v for b in buildings for v in b[:-1]))
        index = {x:i for i, x in enumerate(xs)}
        height = [0] * len(xs)
        H = [(h, x, y) for x, y, h in buildings]
        for h, x ,y in sorted(H):
            // this loop can be replaced by range operation usig segment tree 
            // thus, improves to O(log n) time via lazy propagation
            for i in range(index[x], index[y]):
                height[i] = max(height[i], h)
        ret = []
        for x in xs:
            i = index[x]
            if ret and height[i] == ret[-1][1]: continue
            ret.append([x, height[i]])     
        return ret
```
But the above `O(n^2)` solution got TLE without the implementation of segment tree with lazy propagation.

A faster solution is to keep the alive HIGHEST building in a queue. Pop it up once you pass the right wall of it.
But you don't pop up the building whose height is not the greatest. As the case below shows, the building "under the roof" should be kept in queue until it becomes the highest and the iteration goes beyond the right wall of it.
```
#      ____          ______
#  ___|    |____    |      |
# |   |    |    |   |      |
#1^insert       
#2    ^insert
#3         ^pop     ^found new left wall
#4              ^pop
#5                  ^insert
#6                          ^pop
```  
The code with explanation
```
        n = len(buildings)
        i = 0
        ret, HR = [], []
        while i < n or HR:
            # insert if the new left wall is before or "AT" the right wall of the highest
            if not HR or i < n and buildings[i][0] <= -HR[0][1]: 
                x = buildings[i][0]
                while i < n and buildings[i][0] == x:
                    heappush(HR, (-buildings[i][2], -buildings[i][1]))
                    i += 1
            # pop if the current left wall is strictly after the right wall of the highest
            # i.e. it is time to remove all the buildings before the new left wall
            else:
                x = -HR[0][1]
                while HR and x >= -HR[0][1]:
                    heappop(HR)
            height = len(HR) and -HR[0][0]
            if not ret or height != ret[-1][1]:
                ret.append([x, height])
        return ret
```
LC 850. Rectangle Area II. Return the total area covered by overlapping rectangles.

Discretization along x-dimension and sort along y-dimension. And we iterate through the y-dimension.

When you meet the lower boundary of a rectangle, you increment the count of its discretizied slots (within the lower boundary). When you meet the upper boundary of a rectangle, you decrease the count of its discretizied slots (within the upper boundary). The area between two adjacent `y`s be the height between two `y`s multiples the sum of the "active" slots' width. Using segment tree, we can reduce the time complexity from `O(n^2)` to `O(n log n)`.
```
    def rectangleArea(self, rectangles):
        xs = sorted(set(x for r in rectangles for x in [r[0], r[2]]))
        index = {x:i for i, x in enumerate(xs)}
        count = [0] * len(xs)
        L = []
        for x1, y1, x2, y2 in rectangles:
            L.append((y1, x1, x2, 1))
            L.append((y2, x1, x2, -1))
        ret = y = cur_y = length = 0
        for y, x1, x2, sig in sorted(L):
            ret += (y - cur_y) * length % (1000000007)
            for i in range(index[x1], index[x2]):
                count[i] += sig
            length = sum([x2 - x1 for x1, x2, c in zip(xs, xs[1:], count) if c])
            cur_y = y
        return ret % (1000000007)
```

