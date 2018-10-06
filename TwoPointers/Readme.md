# Two Pointers
Given an array, if all the **sub-optimal solutions** are **continuous subarrays** bounded by indices `l` and `r`, then we can use two pointers to shift `l`, `r` to search for the solution.

C++ template:
```
int i, j;
for (i = 0, j = 0; i < N; ++i) {
    // add A[i] here
    
    while (j <= i && some condition is satisfied) {
        // remove A[j] here
        j++
    }
    
    if (some condition is satisfied) {
        return {j, i};
    }
}
```

Note the order of there operations matter. You should add `A[i]` first, then increment `j` until certain conditions are satisfied.

**LC 567. Permutation in String**

Check if the sub-string of `s2` is a permutation of `s1`. 
Since the question asks for permutation, the order of `s1` does not matter.
If we got too many letters in `s2[l:r]` than `s1[:]`, 
then we increase `l` and remove `s2[l]`; Otherwise, we got insufficent letters, 
we should increase `r` and insert `s2[r]`.

```
    def checkInclusion(self, s1, s2):       
        d = collections.defaultdict(int)
        for c in s1: d[c] += 1
        tmp = collections.defaultdict(int)
        cnt, j = 0, 0     
        for i in range(len(s2)):
            tmp[s2[i]] += 1
            cnt += 1
            while j <= i and tmp[s2[i]] > d[s2[i]]: # becase tmp[c] is always <= d[c]
                tmp[s2[j]] -= 1
                cnt -= 1
                j += 1
            if cnt == len(s1): return True          # only possilbe if tmp[c]==d[c] for all c
        return False
```
