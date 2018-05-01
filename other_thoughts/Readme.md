## Notes
1. Fully exploit the order of your input:
Some questions ask for the maximum sth. while the input is somehow sorted.
You can use the ordering of sorted input.
For example:
```
    # Leetcode 720: longest word with the smallest lexicographical order. 
    # NOTE: lexicographical order is ensured by the sort!
    words.sort()
    ret = ''
    tmp = set([''])
    for word in words:
        if word[:-1] in tmp:
            if len(word) > len(ret):
                ret = word
            tmp.add(word)
    return ret
```
And
* Problem 745 Prefix and Suffix Search - latter word has larger weight
* etc 
 
