## A general approach to backtracking questions (Subsets, Permutations, Combination Sum, Palindrome Partitioning etc.)

Many problems ask for generating all subsets of a set, all permutations or all combinations of candidates etc.
The idea is to use backtracking. But you need a template to do this quickly.
So here is your template.

**LC 78.** Subsets. return all possible subsets (the power set).

Python:
```
    def subsets(self, nums):
        ret = []
        def add(path, nums, i):
            ret.append(path.copy())   # append the current set
            while i < len(nums):
                path.append(nums[i])  # if nums[i] is in the list
                add(path, nums, i + 1)
                path.pop()            # if nums[i] is not in the list
                i += 1
        add([], nums, 0)
        return ret
```

C++
```
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> path;
        vector<vector<int>> ret;
        find(nums, path, ret, 0);
        return ret;
    }
    
    void find(vector<int>& nums, vector<int>& path, vector<vector<int>>& ret, int i) {
        ret.push_back(vector<int>(path.begin(), path.end()));
        for (int j = i; j < nums.size(); ++j) {
            path.push_back(nums[j]);
            find(nums, path, ret, j + 1);
            path.pop_back();
        }
    }
```

**LC 47. Permutations II** Return all possible unique permutations of a list which might contain duplicates. 
```
    def permuteUnique(self, nums):
        ret = []
        N = len(nums)
        nums = sorted(nums)
        
        def add(path, nums, vis):
            if len(path) == N: ret.append(path.copy())
            else:
                for i in range(N):
                    # If the number is a duplicate, it's left number must have been added.
                    # So we avoid adding k out of n numbers (k < n) for comb(n, k) times.
                    # Instead, only the leftmost k are added into the results.
                    if vis[i] or i > 0 and nums[i] == nums[i-1] and not vis[i - 1]: continue
                    
                    path.append(nums[i])
                    vis[i] = True
                    
                    add(path, nums, vis)
                    
                    vis[i] = False
                    path.pop()
        add([], nums, [False] * N)
        return ret
```
