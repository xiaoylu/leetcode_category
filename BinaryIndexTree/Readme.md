## Binary Indexed Trees
BIT computes any prefix sum in `O(log n)` time.

The idea to store the numbers in the way that
* sum of '1', '10', '100' is located at '100'
* sum of '101', '110' is located at '110'

There are update and sum views. 
* The sum view iterates through i -= (i & -i) which removes the last digit 1 in binary presentation. 
* The update view iterates through i += (i & -i) which adds the last digit 1 in binary presentation.
```
    0(root)
    1, 	10, 	100*,        1000          ...
        11,     101, 110*,   1001, 1010,   ...
   		             111*
```
So the update of element with index ‘101’ would be reflected at position 101, 110, 1000, …
When you sum up from index such as ‘111’ through the red path, the update of ‘101’ would be considered at ‘110’.

C++ code: leetcode 307. Range Sum Query - Mutable

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
