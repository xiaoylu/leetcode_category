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
