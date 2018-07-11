## Segment tree
Segment tree stores the interval/segment at each tree node. It supports query of sum/max/min value within a given range of elements.

With segment tree, preprocessing time is `O(n)` and time to for range minimum query is `O(log n)`. The extra space required is `O(n)` to store the segment tree.

As for the array implementation, one important note is that the leaves, which are the array element, are located at i + N. (N is the length and i the index). The index of tree node would be 1, 2\~3, 4\~7, 8\~15 ...
And 0 is a DUMMY node.

Leetcode 307. Range Sum Query - Mutable (Really concise C++ code <http://codeforces.com/blog/entry/18051>
)
```
class NumArray {
public:
    int N, *t;
    NumArray(vector<int> nums) {
        N = nums.size();
        t = new int[2 * N];
        for (int i = 0; i < N; ++i) t[i + N] = nums[i];
        for (int i = N - 1; i > 0; --i) t[i] = t[i << 1] + t[i << 1 | 1];
    }
    void update(int i, int val) {
        for (t[i += N] = val; i > 1; i >>= 1) t[i >> 1] = t[i] + t[i^1];
    }
    int sumRange(int i, int j) {
        int ret = t[j + N];  // Note ret = nums[j] + sum [i,j)
        for (i += N, j += N; i < j; i >>= 1, j >>= 1) {
            if (i&1) ret += t[i++];
            if (j&1) ret += t[--j];
        }
        return ret;
    }
};
```

But one note is that this code does NOT support binary search like classical segment trees (require extra codes). If you need binary search, then a better choice is to construct tree nodes!

Segment Tree also supports range operations (add value to all the elements in a range). But if it's assignment, you need to implement the lazy propagation, otherwise the time complexity is not `O(log n)` anymore. As long as you can stop at some range which is completed covered by the query range, every level of the tree has only two ative nodes for recursion. The time complexity for range operation is `O(log n)`.

See how to construct tree dynamically <https://leetcode.com/problems/my-calendar-iii/discuss/109568/Java-Solution-O(n-log(len))-beats-100-Segment-Tree>

**LC732. My Calendar III** 
Return an integer K representing the largest integer such that there exists a K-booking in the calendar. (There are K books overlapping at the same period.)

```
class MyCalendarThree {
	SegmentTree segmentTree;
    public MyCalendarThree() {
    	segmentTree = new SegmentTree(0, 1000000000);
    }
    public int book(int start, int end) {
        segmentTree.add(start, end, 1);
        return segmentTree.getMax();
    }
}

class SegmentTree {
    TreeNode root;
    public SegmentTree(int left, int right) {
        root = new TreeNode(left, right);
    }
    public void add(int start, int end, int val) {
        TreeNode event = new TreeNode(start, end);
    	add(root, event, val);
    }
    private void add(TreeNode root, TreeNode event, int val) {
        if(root == null) {
            return ;
        }
        /**
         * If current node's range lies completely in update query range.
         */
        if(root.inside(event)) {
            root.booked += val;
            root.savedres += val;
        }
        /**
         * If current node's range overlaps with update range, follow the same approach as above simple update.
         */
        if(root.intersect(event)) {
        	// Recur for left and right children.
            int mid = (root.start + root.end) / 2;
            if(root.left == null) {
                root.left = new TreeNode(root.start, mid);
            }
            add(root.left, event, val);
            if(root.right == null) {
                root.right = new TreeNode(mid, root.end);
            }
            add(root.right, event, val);
            // Update current node using results of left and right calls.
            root.savedres = Math.max(root.left.savedres, root.right.savedres) + root.booked;
        }
    }
    public int getMax() {
        return root.savedres;
    }
    /**
     * find maximum for nums[i] (start <= i <= end) is not required.
     * so i did not implement it. 
     */
    public int get(int start, int right) {return 0;}
	class TreeNode {
	    int start, end;
	    TreeNode left = null, right = null;
	    /**
	     * How much number is added to this interval(node)
	     */
	    int booked = 0;
	    /**
	     * The maximum number in this interval(node). 
	     */
	    int savedres = 0;
	    public TreeNode(int s, int t) {
	        this.start = s;
	        this.end = t;
	    }
	    public boolean inside(TreeNode b) {
	        if(b.start <= start && end <= b.end) {
	            return true;
	        }
	        return false;
	    }
	    public boolean intersect(TreeNode b) {
	    	if(inside(b) || end <= b.start || b.end <= start) {
	            return false;
	        }
	        return true;
	    }
	}
}
```
