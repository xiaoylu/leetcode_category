Parse Strings
===

In order to parse a input with brackets, symbols and numbers, the tricks below may help:

1. Use stacks to store numbers or symbols
2. Load trucks of input at a time. For example, we load a contineous string as the decimal number here.

```
while i < N:
  j = i
  while j < N and S[j].isdigit():
    j += 1
  stack.append( int(S[i:j]) )
  i = j
```

3. Operator Prioriety: when should we combine terms?

Be Lazy: conduct the lower level operations when you have to (i.e. when encoutered high level operations)
