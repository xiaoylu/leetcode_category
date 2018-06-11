## Bit Operations
Basic:
1. Flip `~x`
2. Last 1 `x & -x`
3. First 1
Fill all the postitions by `1`s
```
x |= x >> 16
x |= x >> 8
x |= x >> 4
x |= x >> 2
x |= x >> 1
```
then `x ^ (x >> 1)`

4. Magic
```
 (x ^ y) ^ y = x
 (x ^ y) ^ x = y 
```
so if you want to find the `x` which XOR `y` gives `s`, then
```
x^s 
```
returns `y`
