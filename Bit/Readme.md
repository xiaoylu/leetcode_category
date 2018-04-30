## Notes
1. Magic
```
 (x ^ y) ^ y = x
 (x ^ y) ^ x = y 
```
so if you want to find the `x` which XOR y gives `s`, then
```
x^s 
```
returns `y`
