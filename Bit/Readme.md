# Bit Operations

## Basic operations:
* 1. Flip `~x`
* 2. Get the rightmost **set bit** `x & -x`
* 3. Fill all the postitions by `1`s
```
x |= x >> 16
x |= x >> 8
x |= x >> 4
x |= x >> 2
x |= x >> 1
```
* 4. Get the left-most set bit step3 + `x ^ (x >> 1)`
* 5. Test if an interger `2**k - 1` (all ones in binary form) `~x == 0`
* 6. Number of set bit `__builtin_popcount(int x)` (C++ CPU specific instruction)
* 7. Remove the last set bit `x&(x-1)`
* 8. Test if `1000..00`, `x&(x-1)==0`
* 9. Remove some bit `A &= ~(1 << bit)`
* 10. Get all 1-bits `~0`

## Templates:

### Single number problem by XOR
Given an array of integers, every element appears `k (k > 1)` times except for one, which appears `p` times `(p >= 1, p % k != 0)`. Find that single one.

We count the number of occurrence of `1`s on each digit. Say, for a particular digit, the input array contains `w*k + p` ONEs at this digit, then, the number which repeats `p` times has a One at this digit. Otherwise, the input array contains `w*k` ONEs, then, the number which repeats `p` times has a ZERO at this digit.

Note that we do not need to count ZEROs because the input array should has a size mod `k` equal to `p`.

Java Code for the case `k = 3, p = 1`. We need two 32-bits variable to store the occurrence of `1`s on each digit, which ranges from `0b00` to `0b10` (`00->01->10->00`). Note `11` is `00` here.

***LC 137. Single Number II***

```
    x1 = 0
    x2 = 0
    for (int i : nums) {
        x2 ^= x1 & i;
        x1 ^= i;
        mask = ~(x1 & x2);
        x2 &= mask;
        x1 &= mask;
    }
    return x1
```

If there are two numbers, we can divide the input array into two groups. If we know `x1^x2 > 0`, we know they must be different at one bit (ex. the rightmost set bit of `x1^x2`). Then we go ahead to XOR each group.

***LC 260. Single Number III***

```
    diff = reduce(lambda x,y: x^y, nums)
    diff &= -diff
    x1, x2 = 0, 0
    for n in nums:
        if n & diff:
            x1 ^= n
        else:
            x2 ^= n
    return [x1, x2]
```

### Bit Masks
Mask allows you to have a small subset (no more than 32 elements for intergers) but could be larger using C++ bit_set or larger numbers in Python.

Three convenient operations:
```
Set union A | B
Set intersection A & B
Set subtraction A & ~B
```
First, it allows dynamic programming to know the states quickly. Secondly, the shift of bits usually can be treated as a `O(1)` operation.

**LC 318. Maximum Product of Word Lengths** Find the maximum value of `length(word[i]) * length(word[j])` where the two words do NOT share common letters.
```
    def maxProduct(self, words):
        d = {}
        for w in words:
            mask = 0
            for c in set(w):
                mask |= 1 << (ord(c) - 90)
            d[mask] = max(d.get(mask, 0), len(w))
        return max([d[x] * d[y] for x in d for y in d if not x&y] or [0])
```

**847. Shortest Path Visiting All Nodes** Return shortest path that visits every node in a graph (NP-hard problem)
The idea is to store all the visited nodes and the current node in a 2D matrix and solve by dynamic programming
```

```
