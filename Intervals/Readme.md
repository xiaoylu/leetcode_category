# Intervals

## Discretization
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
The sorting can also be done for the upper bound. It is more convenient for the intersection problems.

**452. Minimum Number of Arrows to Burst Balloons** 

Find the min size of `S` such that each interval contains at least one element of `S`. Note you need to sort by upper bound, but not lower bound. Think about why?
```
    def findMinArrowShots(self, points):
        ret, end = 0, -float('inf')
        for l, r in sorted(points, key = lambda x: x[1]):
            if l > end:
                ret += 1
                end = r
        return ret
```

**757. Set Intersection Size At Least Two**

Extension of LC 452 that each interval contains at least two elements of `S`. Same idea, but sort by `(upper bound, -lower bound)`. e.g `[[1,5],[4,5],[5,9],[7,9],[9,10]] => [[4,5], [1,5], [7,9], [5,9] , [9,10]]`. [Idea]<https://leetcode.com/problems/set-intersection-size-at-least-two/discuss/113086/Hope-you-enjoy-this-problem.-:-)-O(NlogN)JavaGreedy-Easy-to-understand-solution>


While the first operation is very common, another important skill is "Discretization". 
We record the independent "time slots" formed by all the starts and ends. (Not necessarily the ends are after starts)
Get a `count` array for each slot, when an interval comes in, add `count[i]` for all slot `i` inside this interval.
You will know the maximum number of one slot occupied by the intervals. This number is the result.

**LC 253. Meeting Rooms II.** 
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

**LC 218. The Skyline Problem.**
The skyline is the outer contour of building roofs.
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

**LC 850. Rectangle Area II.**
Return the total area covered by overlapping rectangles.

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

## Merging Intervals by BST

How to merge a new interval `[l, r)` with the previous ones in `O(log N)` time?

You can use a `map<int, int>` in C++ or `TreeMap<Integer, Integer>` in Java to maintain the intervals. (Key being `l` and value being `r`)

But you need to pay extra attention to the corner cases:
* what if the `l` is the smallest?
* what if the `r` is the largest?
* what if there is no overlapping intervals with `[l, r]`?

Python code: (embrassingly `O(n)` time insertion due to lack of default BST)
```
// S and E are the lists of the starts and ends. 
i = bisect.bisect_left(S, start)

// check if the previous interval overlaps with [start, end]
if self.S and i > 0 and self.E[i-1] + 1 >= start: i -= 1

// delete all the overlapping intervals
j = i
while j < len(self.S) and self.S[j] <= end + 1:
    start = min(start, self.S[j])
    end = max(end, self.E[j])
    j += 1
del self.S[i:j]
del self.E[i:j]

// insert new interval
self.S.insert(i, start)
self.E.insert(i, end)
```

C++ code for insertion: (`O(log n)` time with STL map)
```
auto it = m.lower_bound(val);
if (m.size() && it != m.begin() && (--it)->second + 1 < val) ++it; // check left
while (it != m.end() && end + 1 >= it->first) {
    start = min(start, it->first);
    end = max(end, it->second);
    it = m.erase(it);
}
m.emplace_hint(it, start, end);
```

C++ code for removal (`O(log n)` time with STL map)
```
if (m.empty()) return;
auto l = m.lower_bound(left);
auto r = m.upper_bound(right);

if (l != m.begin() && (--l)->second < left) ++l;

if (l == r) return; // Important!!! check if the removal interval overlaps with any other intervals

int ll = min(l->first, left), rr = max((--r)->second, right);

m.erase(l, ++r);

if (ll < left) m[ll] = left;
if (rr > right) m[right] = rr;
```


**NOTE**: Both C++'s and Python's function `insert`/`emplace` use a hint position **follow** the new location of the inserted. That being said, the newly inserted element would be at this position after the insertion is done. Besides, for sorted structures like `map` and `set` in C++, this position is **merely a hint**.

**LC 715. Range Module**

```
class RangeModule {
public:
    // add elements in the input range
    void addRange(int left, int right) {
        auto l = invals.upper_bound(left), r = invals.upper_bound(right); 
        if (l != invals.begin()) {
            l--;
            if (l->second < left) l++;
        }
        if (l != r) {
            left = min(left, l->first);
            right = max(right, (--r)->second);
            invals.erase(l,++r);
        }
        invals[left] = right;
    }
    
    // to check if all elements in the range exist
    bool queryRange(int left, int right) {
        auto it = invals.upper_bound(left);
        if (it == invals.begin() || (--it)->second < right) return false;
        return true;
    }
    
    // remove elements in the range
    void removeRange(int left, int right) {
        auto l = invals.upper_bound(left), r = invals.upper_bound(right); 
        if (l != invals.begin()) {
            l--;
            if (l->second < left) l++;
        }
        if (l == r) return;
        int l1 = min(left, l->first), r1 = max(right, (--r)->second);
        invals.erase(l, ++r);
        if (l1 < left) invals[l1] = left;
        if (r1 > right) invals[right] = r1;
    }
private:
    map<int, int> invals;
};
```

**LC 352. Data Stream as Disjoint Intervals**

Same problem as above, just need to add intervals.

Java:
```
public class SummaryRanges {
    TreeMap<Integer, Interval> tree;

    public SummaryRanges() {
        tree = new TreeMap<>();
    }

    public void addNum(int val) {
        if (tree.containsKey(val)) return;
        Integer l = tree.lowerKey(val);
        Integer h = tree.higherKey(val);
        if(l != null && h != null && tree.get(l).end + 1 == val && h == val + 1) {
            tree.get(l).end = tree.get(h).end;
            tree.remove(h);
        } else if(l != null && tree.get(l).end + 1 >= val) {
            tree.get(l).end = Math.max(tree.get(l).end, val);
        } else if(h != null && h == val + 1) {
            tree.put(val, new Interval(val, tree.get(h).end));
            tree.remove(h);
        } else {
            tree.put(val, new Interval(val, val));
        }
    }

    public List<Interval> getIntervals() {
        return new ArrayList<>(tree.values());
    }
}
```

C++
```
class SummaryRanges {
public:    
    void addNum(int val) {
        int start = val, end = val;
        auto it = m.lower_bound(val);
        if (m.size() && it != m.begin() && (--it)->second + 1 < val) ++it;
        while (it != m.end() && end + 1 >= it->first) {
            start = min(start, it->first);
            end = max(end, it->second);
            it = m.erase(it);
        }
        m.emplace_hint(it, start, end);
    }
    
    vector<Interval> getIntervals() {
        vector<Interval> R;
        for (const auto& it : m) R.emplace_back(Interval(it.first, it.second));
        return R;
    }
    
private:
    map<int, int> m;
};
```




