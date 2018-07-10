# Binary Search

## Basics
For complicated problems, you can call
* Python `bisect.bisect_right(s, ele)` 
* C++ `upper_bound(s.begin(), s.end(), ele)`
as a sub-procedure to do binary search. 

**Note** the difference of Python `bisect_right` vs. `bisect_left` is the same as C++ `lower_bound` vs. `upper_bound`.

`bisect_right` and `upper_bound` return what ***comes after (to the right of) any existing entries.***

If needed, you can customize your own binary searching. Here, you need to identify the style suits your problem better
```
  array.sort()
  l, r = 0, len(array) # NOTE never try array[r] in this case
  while l < r:
    mid = (l + r) // 2
    if array[mid] >= target: # NOTE when not target found,
                             # equal make sure search ending up with an element GREATER than target.
      r = mid
    else:
      l = mid + 1
  # NOW, l=r and array[r]==target
  return l
```
The first style solves most problems, while another style allows access to `array[r]`.
Useful for problem like "min element in rotated array".
```
  array.sort()
  l, r = 0, len(array) - 1 
  while l <= r:
    mid = (l + r) // 2

    if array[mid]==target:
      return mid # return when found target

    # NOTE you can access array[r] in this case, useful for problem like "min element in rotated array"

    if array[mid] > target:
      r = mid - 1
    else:
      l += mid + 1 

  # NOW, l=r+1 and target is not found
  return l
```

## Balanced BST
To keep a binary search tree balanced, it should be implemented as Red-Black tree, AVL tree or even skipping lists (probablistics) to maintain the similar heights of the branches sharing the same parent.

**LC 220. Contains Duplicate III**
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between `nums[i]` and `nums[j]` is at most t and the absolute difference between i and j is at most k.

Due to the lack of equivalent container, Python code needs to use Buckets (using collections.OrderedDict). 
C++ and Java are good for this problem thanks to `TreeSet<Integer>` (Java) and `set<long>` (C++).

C++ solution:
```
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        set<long> win;
        for (int i = 0; i < nums.size(); ++i) {
            if (i > k) win.erase(nums[i - k - 1]);
            auto lower = win.lower_bound((long)nums[i] - t);
            
            # If *lower == nums[i] - t, then almost duplicate due to the lower bound
            # Since *lower >= nums[i] - t, so if *lower < nums[i] + t, 
            # then almost duplicate due to the upper bound
            if (lower != win.end() && abs(*lower - nums[i]) <= t) return true;
            win.insert(nums[i]);
        }
        return false;
    }
```

## More advanced
Binary search is a universal treatment for problems with **monotonic solutions**. The KEY is to identify the monotonic natural of these problems. Usually, if the solution is among a ordered list, the answer would be `Yes` before a certain number and `N` after a certain number. And you job to find the last `Y` or the first `N`.
```
1 2 3 4 5 6 7
Y Y Y N N N N
```
It is usually fast to check the correctness of your solution. So you can binary-search the solution, if wrong, just jump to the middle one.

**"410. Split Array Largest Sum"**: given the largest sum, you can check if spliting the array into k subarrays are possible in `O(n)` time.

**"786. K-th Smallest Prime Fraction"**: given the smallest prime fraction, you can check if there are `K` pairs whose prime fraction is smaller than the given value in `O(n)` time.  

**"373. Find K Pairs with Smallest Sums"**: given the smallest sum, you can check if there are `K` pairs whose sum is smaller in `O(n)` time.

Other problems:
* LC774 Minimize Max Distance to Gas Station
* LC378 Kth Smallest Element in a Sorted Matrix
* LC668 Kth Smallest Number in Multiplication Table
* LC719 Find K-th Smallest Pair Distance

On the other hand, Priority Queue can be used for many of such problems. Details see this post <https://leetcode.com/problems/k-th-smallest-prime-fraction/discuss/115819/Summary-of-solutions-for-problems-%22reducible%22-to-LeetCode-378>.

## Some details about `bisect_right` and `bisect_left`
Source code <https://github.com/python/cpython/blob/master/Lib/bisect.py>
```
    # bisect_left()
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x: lo = mid+1
        # MOVE hi in the case of equality 
        # 0 1 2 3 3 3 4 5
        #       ^
        #       hi would end up staying here when searching for 3.
        else: hi = mid
    return lo
```
`bisect_right()` is similar to `bisect_left()`, but returns an insertion point which comes after (to the right of) any existing entries of x in a.
```
    # bisect_right()
    while lo < hi:
        mid = (lo+hi)//2
        # MOVE lo in the case of equality 
        if a[mid] <= x: lo = mid+1
        # 0 1 2 3 3 3 4 5
        #             ^
        #             hi would end up staying here when searching for 3.
        else: hi = mid
    return lo
```
