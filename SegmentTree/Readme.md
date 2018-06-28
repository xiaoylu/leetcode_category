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

Segment Tree support range operations (such as increase the element from index `i` to `j` by one). But you need to implement the lazy propagation, otherwise the time complexity is not `O(log n)` anymore.


Segment Tree + MergeSort = MergeSort Tree

Segment Tree + ..

