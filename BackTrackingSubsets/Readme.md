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

**LC 39. Combination Sum** Find all unique combinations in candidates where the candidate numbers sums to target.
```
    def combinationSum(self, nums, target):
        nums = sorted(nums)  
        ret = []
        def find(path, cur_sum, j):
            if cur_sum == target:
                ret.append(path.copy())
            elif cur_sum > target:
                return
            for i in range(j, len(nums)):
                path.append(nums[i])
                find(path, cur_sum + nums[i], i) # allow access to the same candidate for multiple times
                path.pop()
        find([], 0, 0)
        return ret
```

**LC 131. Palindrome Partitioning** Return every partition a string such that each substring of the partition is a palindrome. Ex. "abb" => `['a', 'bb']` + `['a', 'b', 'b']`
```
    def partition(self, s):
        ret = []
        def find(s, path):
            if not s:
                ret.append(path.copy())
            for i in range(1, len(s) + 1):
                if s[:i] == s[i-1::-1]:
                    find(s[i:], path + [s[:i]])
        find(s, [])
        return ret
```

This problem has another version: return the minimum number of cuts s.t. each cut is a palindrome. DP solution: keep extending the last cut, and update the dp[j] if last cut reaches index j.

**LC 784. Letter Case Permutation** Transform every letter individually to be lowercase or uppercase, return all combinations.
Input: S = "a1b2"
Output: `["a1b2", "a1B2", "A1b2", "A1B2"]`

```
    def letterCasePermutation(self, S):
        ret = []
        def change(ret, S, i):
            while i < len(S) and S[i].isdigit(): i += 1
            ret.append("".join(S))
            for j in range(i, len(S)):
                if S[j].isalpha():
                    S[j] = S[j].upper()
                    change(ret, S, j + 1)
                    S[j] = S[j].lower()
        change(ret, list(S.lower()), 0)
        return ret
```

**LC 320. Generalized Abbreviation**
Input: "word"
Output:`["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]`
```
    def generateAbbreviations(self, word):
        def dfs(ret, path, word, i):
            if i == len(word):
                ret.append("".join(path))
            else:
                # add a letter 
                path += word[i], 
                dfs(ret, path, word, i + 1)
                path.pop()
                # add a number only at the beginning or with a previous letter (no adjacent numbers)
                if not path or path[-1].isalpha():
                    for j in range(i, len(word)):
                        path += str(j - i + 1),
                        dfs(ret, path, word, j + 1)
                        path.pop()
        ret = []
        dfs(ret, [], word, 0)
        return ret
```
