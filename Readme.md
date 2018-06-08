## Binary Indexed Trees
The idea is that to sum up the numbers before '111', you just need:
* sum of '1', '10', '11', '100', which is stored at '100'
* sum of '101', '110', which is stored at '110'

There are update and sum views.
For the sum view, we iteratively remove the last digit 1 in binary presentation by i -= (i & -i). 
For the update view, we iteratively adds the last digit 1 in binary presentation by i += (i & -i).
```
root      0
level1    1, 	10, 	100*,       1000          ...
level2        11,   101, 110*,  1001, 1010,   ...
   		                   111*
```
So the update of element with index ‘101’ would be reflected at position 101, 110, 1000, …
When you sum up from index such as ‘111’ through the '*' path, the update of ‘101’ would be included at ‘110’, 
the update of '11' would be included at '100', so on so forth.

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
