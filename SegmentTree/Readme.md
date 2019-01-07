## Segment tree (supporting range operation)
Segment tree supports the update and query of sum/max/min value within a given range of elements.

* The "best" C++ introduction [by (DarthPrince)](http://codeforces.com/blog/entry/15729)
* Really concise C++ code <http://codeforces.com/blog/entry/18051>
* Construct tree dynamically using [Java](https://leetcode.com/problems/my-calendar-iii/discuss/109568/Java-Solution-O(n-log(len))-beats-100-Segment-Tree)

You can even do binary search in segment trees using the sum value at each segment tree node!

Segment Tree supports range operations. We go from root to leaves, when one interval is **completed covered** by the query range, we can stop there and save the updates as lazy value. The next time when we need to go down through that node, we can carry such lazy value down to the children. In this way, every level of the tree has only two active nodes. The time complexity for range operation is the tree depth `O(log N)` where `N` is the size of the range.

**LC732. My Calendar III** 
Return an integer K representing the largest integer such that there exists a K-booking in the calendar. (There are K books overlapping at the same period.)

Concise Python:        
```
class MyCalendarThree(object):

    def __init__(self):
        self.seg = collections.defaultdict(int)
        self.lazy = collections.defaultdict(int)
        
    def book(self, start, end):
        def update(s, e, l = 0, r = 10**9, ID = 1):
            if r <= s or e <= l: return 
            if s <= l < r <= e:
                self.seg[ID] += 1
                self.lazy[ID] += 1
            else:
                m = (l + r) // 2
                update(s, e, l, m, 2 * ID)
                update(s, e, m, r, 2*ID+1)
                self.seg[ID] = self.lazy[ID] + max(self.seg[2*ID], self.seg[2*ID+1])
        update(start, end)
        return self.seg[1] + self.lazy[1]
```
The usage of ID is similar to the index of array element in a heap -- 2ID and 2ID+1 are the indices of the two kids.
ex. 1 is the root, 2, 3 are the left and right kids of root, so on so forth.

Time complexity O(1) - In each update, only two nodes can be active at every level of the segment tree. Since the segment tree has max range `[0, 10**9)`, the depth of segment tree is `log(10**9) = O(1)`.

**LC 307. Range Sum Query - Mutable**
```
class NumArray(object):
    def __init__(self, nums):
        self.seg = collections.defaultdict(int)
        for i, n in enumerate(nums): self.update(i, n)

    def update(self, i, val, l = 0, r = 10**9, ID = 1):
        if l == i == r - 1:
            self.seg[ID] = val
        else:
            m = (l + r) // 2
            if i < m: self.update(i, val, l, m, 2 * ID)
            else:     self.update(i, val, m, r, 2*ID + 1)
            self.seg[ID] = self.seg[2*ID] + self.seg[2*ID+1]

    def sumRange(self, i, j, l = 0, r = 10**9, ID = 1):
        if ID == 1: j += 1 # make the input range inclusive-exclusive [i, j] --> [i,j)
            
        if j <= l or r <= i: return 0
        if i <= l < r <= j: return self.seg[ID]
        m = (l + r) // 2
        return self.sumRange(i, j, l, m, 2*ID) + self.sumRange(i, j, m, r, 2*ID+1)
```

## Range sum with lazy operation
C++ code from [C++ by (DarthPrince)](http://codeforces.com/blog/entry/15729)
```
// A function to update a node :
void upd(int id,int l,int r,int x){//	increase all members in this interval by x
	lazy[id] += x;
	s[id] += (r - l) * x;
}

// A function to pass the update information to its children :
void shift(int id,int l,int r){//pass update information to the children
	int mid = (l+r)/2;
	upd(id * 2, l, mid, lazy[id]);
	upd(id * 2 + 1, mid, r, lazy[id]);
	lazy[id] = 0;// passing is done
}

// A function to perform increase queries :
void increase(int x,int y,int v,int id = 1,int l = 0,int r = n){
	if(x >= r or l >= y)	return ;
	if(x <= l && r <= y){
		upd(id, l, r, v);
		return ;
	}
	shift(id, l, r);
	int mid = (l+r)/2;
	increase(x, y, v, id * 2, l, mid);
	increase(x, y, v, id*2+1, mid, r);
	s[id] = s[id * 2] + s[id * 2 + 1];
}
```
Note that `shift` should be called at every level right **before** the function `increase` traverses to the children!

**LC 699. Falling Squares**

俄罗斯方块堆箱子，求每一块放下后的最高高度

输入格式为［［左边界，宽度］,......]

Input: [[1, 2], [2, 3], [6, 1]]

Output: [2, 5, 5]

Explanation:

After the first drop of positions[0] = [1, 2]:
```
_aa
_aa
-------
The maximum height of any square is 2.
```

After the second drop of positions[1] = [2, 3]:
```
__aaa
__aaa
__aaa
_aa__
_aa__
--------------
```
The maximum height of any square is 5.  

```
class Solution:
    def fallingSquares(self, positions):
        v = collections.defaultdict(int)
        lazy = collections.defaultdict(int)
        
        def query(x, y, l = 0, r = 2046, ID = 1):
            if y <= l or x >= r: return float('-inf')
            if x <= l < r <= y: return v[ID]
            # note the lazy propagation before quering kids
            shift(l, r, ID)
            m = (l + r) // 2
            return max(query(x, y, l, m, 2 * ID), query(x, y, m, r, 2*ID+1))
        
        def upd(l, r, ID, val):
            v[ID] = max(v[ID], val)
            lazy[ID] = max(lazy[ID], val)
            
        def shift(l, r, ID):
            m = (l + r) // 2
            upd(l, m, 2*ID, lazy[ID])
            upd(m, r, 2*ID+1, lazy[ID])
            lazy[ID] = float('-inf')
        
        def add(x, y, val, l = 0, r = 2046, ID = 1):
            if y <= l or x >= r: return
            if x <= l < r <= y:
                upd(l, r, ID, val)
                return
            
            shift(l, r, ID)    
            m = (l + r) // 2
            add(x, y, val, l, m, 2 * ID)
            add(x, y, val, m, r, 2*ID+1)
            v[ID] = max(v[2*ID], v[2*ID+1])
        
        L = list(set([j for i, side in positions for j in [i, i+side]]))
        L.sort()
        indice = {x:i for i, x in enumerate(L)}
        
        R = []
        for i, side in positions:
            x, y = indice[i], indice[i+side]          
            add(x, y, side + query(x, y))
            R.append(v[1])
        return R
```

## Two-dimensional Segment Tree

A segment tree over `x` coordinates. Each node of the x-coordinate (outer) segment tree stores a segment tree on `y` coordinates that corresponds to "strip" `[xl, xr]`, meaning that it will store all the sums of rectangles `[xl,xr]×[yl,yr]` where `[yl,yr]` is a valid atomic segment tree segment.

While answering queries you basically first traverse by outer tree until you find `O(logn)` segments that fits your x-part-of-a-query and then for each such segment you are traversing in corresponding segment tree until you find a set of segments that match your y-part-of-a-query.

"Before writing a 2D-segment tree you should consider using partial sums, 2D-Fenwick tree or O(1)-static-rmq for 2D since all of them are like 10× shorter and usually faster." ---- cited from a Quora answer by an ACMer
