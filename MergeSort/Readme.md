## Merge Sort
C++ provides built-ins for merge sort including:
* `merge(l1.begin(), l1.end(), l2.begin(), l2.end(), result.begin());`
* `inplace_merge(l.begin(), l.middle, l.end())` `[begin, middle)` merges with `[middle, end)`

Merge Sort is suitable for problems which looks for some pairs 
s.t. i < j, and nums[i], nums[j] satisfy some constraints.

We can find such pairs when `i` is in the left subarray, and `j` is in the right subarray.

LeetCode 493. Reverse Pairs. Return the number of reverse pairs s.t. `i < j` and `nums[i] > 2*nums[j]`.
```
    int sort_count(vector<int>::iterator begin, vector<int>::iterator end) {
        if (end - begin <= 1) return 0;
        vector<int>::iterator middle = begin + (end  - begin) / 2;
        int count = 0;
        if (begin < middle) count += sort_count(begin, middle);
        if (middle < end) count += sort_count(middle, end);
        vector<int>::iterator i, j;
        for (i = begin, j = middle; i < middle; ++i) { // double pointers trick
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

LeetCode 327. Count of Range Sum. Return the number of range sums that lie in `[lower, upper]` inclusive.
```
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        int n = nums.size();
        vector<long> sums(n + 1, 0);
        for (int i = 0; i < n; ++i) sums[i + 1] = sums[i] + nums[i];
        return sort_count(sums, 0, n + 1, lower, upper);
    }
    
    int sort_count(vector<long>& sums, int l, int r, int lower, int upper) {
        if (r - l <= 1) return 0;
        int m = (l + r) / 2, i, j1, j2;
        int count = sort_count(sums, l, m, lower, upper) + sort_count(sums, m, r, lower, upper);
        for (i = l, j1 = j2 = m; i < m; ++i) { // we have two j pointers and one i pointer
            while (j1 < r && sums[j1] - sums[i] < lower) j1++; 
            while (j2 < r && sums[j2] - sums[i] <= upper) j2++;
            count += j2 - j1;
        }
        inplace_merge(sums.begin() + l, sums.begin() + m, sums.begin() + r);
        return count;
    }
```

LeetCode 315. Count of Smaller Numbers After Self
```
    #define iterator vector<vector<int>>::iterator
    void sort_count(iterator l, iterator r, vector<int>& count) {
        if (r - l <= 1) return;
        iterator m = l + (r - l) / 2;
        sort_count(l, m, count);
        sort_count(m, r, count);
        for (iterator i = l, j = m; i < m; i++) {
            while (j < r && (*i)[0] > (*j)[0]) j++;
            count[(*i)[1]] += j - m; // add the number of valid "j"s to the indices of *i
        }
        inplace_merge(l, m, r);
    }
    vector<int> countSmaller(vector<int>& nums) {
        vector<vector<int>> hold;
        int n = nums.size();
        for (int i = 0; i < n; ++i) hold.push_back(vector<int>({nums[i], i})); // "zip" the nums with the indices
        vector<int> count(n, 0);
        sort_count(hold.begin(), hold.end(), count);
        return count;
    }
```

Such problems do not care about the position of the pairs. The `j > i` could be possibly anywhere after `i`. This is the KEY feature, so we insert the elements one-by-one, sort the arrays after 'i' and search for those valid `j`s. Of course, balanced BST would work for this purpose, but it requires extra code to store the size of each tree branch. 

Merge sort avoids extra data structure for this. For problems like these, Segment Tree and Binary Indexed Tree are also good choices. But for code interviews, merge sort code is easier and you can mention ST, BIT to get more credits.


