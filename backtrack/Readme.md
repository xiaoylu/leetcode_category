## NOTES
1. Two styles of backtracking (Example: N-Queen)
**recursive**
```
    def nqueens(n):
        def valid(a,b,i,j):
            return (a!=i) and (b!=j) and (abs(a-i)!=abs(b-j))
        
        self.ret = 0
        def dfs(path):
            if len(path)==n:
                self.ret += 1
                return
            row = len(path)
            for col in range(n):
                if all(valid(row,col,i,j) for i,j in enumerate(path)):
                    dfs(path+[col])
        dfs([])
        return self.ret
```

**Iterative**
```
    ans =[[]]
    for row in range(n):
        new_ans = []
        for path in ans:
            for col in range(n):
                if all(valid(row,col,i,j) for i,j in enumerate(path)):
                    new_ans.append(path+[col])
        ans = new_ans
    return len(ans)
```

2. How to avoid duplicates in backtracking? 
```
        # 47. Permutations II
        # Given a collection of numbers that might contain duplicates, 
        # return all possible unique permutations.
        ret = [[]]
        for n in nums:
            new_ret = []
            for row in ret:
                for i in range(len(row)+1):
                    new_ret.append(row[:i]+[n]+row[i:])
                    # Note: avoid inserting a number before any of its duplicates!!
                    if i < len(row) and row[i]==n: 
                        break
            ret = new_ret
        return ret
```

```
        # 40. Combination Sum II
        # Find all unique combinations in candidates where the candidate numbers sums to target
        candidates.sort()
        ret = []
        def dfs(target, path, start):
            if target < 0 or (start==len(candidates) and target != 0):
                return
            if target == 0:
                ret.append(path)
                return
            for i in range(start, len(candidates)):
                # NOTE: the key to avoid duplicates!!
                if i > start and candidates[i]==candidates[i-1]: continue 
                dfs(target-candidates[i], path+[candidates[i]], i+1)
        dfs(target, [], 0)
        return ret
```
