## Binary Indexed Trees (Fenwick Tree)

Fenwick tree supports the query of array prefix sums in `O(log N)` time.

The idea is to sum up the elements with index less than '0b111' (index number in binary), you need to know:
* sum of elements at '1', '10', '11', '100', which is stored at node '100'
* sum of elements at '101', '110', which is stored at node '110'

The sum of these partial sums would be the results. Since there are at most `O(log N)` such partial sums, each query takes `O(log N)` time.

There are update and sum views.

For the sum view, we iteratively remove the last digit 1 of `i` by `i -= (i & -i)` until `i = 0`. 

For the update view, we iteratively adds the last digit 1 of `i` by `i += (i & -i)` until `i > N`.

NOTE, the node `0` is a dummy node.

```
root      0
level1    1, 	10, 	100*,       1000          ...
level2        11,   101, 110*,  1001, 1010,   ...
   		                   111*
```
At `111` stores the partial sum at `111`.
At `110` stores the partial sum at `110`, `101`.
At `100` stores the partial sum at `100`, `11`, `10`, `1`.
When you sum up from index such as `111` through the `*` path, these partial sums are included.

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
        val -= sumk(i) - sumk(i-1);
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
