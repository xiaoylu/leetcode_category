## Merge Sort
C++ provide build-ins for merge sort including:
* `merge(l1.begin(), l1.end(), l2.begin(), l2.end(), result.begin());`
* `inplace_merge(l.begin(), l.middle, l.end())` [begin, middle) merges with [middle, end)

Merge Sort is suitable for problems which looks for some pairs 
s.t. i < j, and nums[i], nums[j] satisfy some constraints.

We can find such pairs when i is in the left subarray, and j is in the right subarray.

LeetCode 493. Reverse Pairs
```
    int sort_count(vector<int>::iterator begin, vector<int>::iterator end) {
        if (end - begin <= 1) return 0;
        vector<int>::iterator middle = begin + (end  - begin) / 2;
        int count = 0;
        if (begin < middle) count += sort_count(begin, middle);
        if (middle < end) count += sort_count(middle, end);
        vector<int>::iterator i, j;
        for (i = begin, j = middle; i < middle; ++i) {
            while (j < end && *i > 2L * *j) {
                j++;
            }
            count += j - middle;
        }
        inplace_merge(begin, middle, end);
        return count;
    }
    int reversePairs(vector<int>& nums) {
        return sort_count(nums.begin(), nums.end());
    }
```

LeetCode 327. Count of Range Sum
