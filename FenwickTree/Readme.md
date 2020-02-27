## Binary Indexed Trees (Fenwick Tree)

Fenwick tree supports the query of array prefix sums in `O(log N)` time. Specifically, given an array `A` of length `N`, Fenwick tree returns the prefix sum of `A[:k]` for any `0<=k<=N` in `O(log N)` time, while the elements of `A` can also be updated dynamically in `O(log N)` time. 

The idea is to maintains the partial sums.

To sum up all elements with index less than '0b111' (presented in binary, 1-indexed instead of 0-indexed), we need to know:
* sum of the elements at '1', '10', '11', '100', which is stored at node '100'
* sum of the elements at '101', '110', which is stored at node '110'

The sum of these partial sums would be the sum of `A[0b1] + A[0b10] + ... + A[0b111]`. 

Since there are at most `O(log N)` such partial sums, each query takes `O(log N)` time.

NOTE, the node `0` is a dummy node and the tree is 1-indexed (instead of 0-indexed)

```
// marked (*) nodes stores the prefix sum for elements with index less than `0b111`
root      0
          |--------------------- ...
          |  |  |         |
level1    1  10 100*      1000          
             |  |----     |--------- ...
             |  |   |     |     |
level2       11 101 110*  1001  1010   ...
                    |          |
                    111*
```
At `111` stores the partial sum of `111`.
At `110` stores the partial sum of `110`, `101`.
At `100` stores the partial sum of `100`, `11`, `10`, `1`.

Sum up these partial sums (marked by `*`), and we will obtain prefix sum `A[0b1]+A[0b10]+...+A[0b111]`.

Two Operations:

* To obtain the prefix sum `A[0:i]`, we start from index `i` and iteratively remove the last digit 1 of `i` by `i -= (i & -i)` until `i = 0`. This step is illustrated by the diagram above.

* To update `A[i-1]`, we start from index `i` (instead of `i-1` because the tree is 1-indexed), and then iteratively adds the last digit 1 of `i` by `i += (i & -i)` until `i > N`. We update the associated partial sums along this path by the change of `A[i-1]`.

**LC 307. Range Sum Query - Mutable**

C++ code: 
```
class NumArray {
public:
    vector<int> bi;
    int n;
    NumArray(vector<int> nums) {
        n = nums.size();
        bi.resize(n + 1, 0);
        fill(bi.begin(), bi.end(), 0);
        for (int i=0;i<n;++i) {
            update(i, nums[i]);
        }
    }
    
    void update(int i, int val) {
        i++; // dummy node ZERO 0
        val -= sumk(i) - sumk(i-1);  // compute the relative change
        while(i <= n)
        {
            bi[i] += val;
            i+= (i&-i);
        }
    }
    
    int sumRange(int i, int j) { // Inclusive? Yes, [i,j]
        return sumk(j+1) - sumk(i);
    }
    
private:
    int sumk(int k) { // [0, k)
        int ret = 0;
        while (k) {
            ret += bi[k];
            k -= (k&-k);
        }
        return ret;
    }
};
```
