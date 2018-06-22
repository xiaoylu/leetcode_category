## Bit Operations

# Basic operations:
* 1. Flip `~x`
* 2. Last 1 `x & -x`
* 3. Fill all the postitions by `1`s first
```
x |= x >> 16
x |= x >> 8
x |= x >> 4
x |= x >> 2
x |= x >> 1
```
* 4. get the first 1: fill all ones (step 3) and `x ^ (x >> 1)`
* 5. Test if an interger `2**k - 1` (all ones in binary form) `~x == 0`


# Templates:
Given an array of integers, every element appears `k (k > 1)` times except for one, which appears `p` times `(p >= 1, p % k != 0)`. Find that single one.

We count the number of occurrence of `1`s on each digit. Say, for a particular digit, the input array contains `w*k + p` elements who get a ONE at this digit. Then, we are sure the number which appears `p` times has a One at this particular digit.
Note that we do not need to count ZEROs because the input array should has a size mod `k` equal to `p`.

Java Code for the case `k = 3, p = 1`
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
