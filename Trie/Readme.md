## Notes
1. Easy creation of Prefix Tree
```
    node = self.root
    for c in word+"$":
        node = node.setdefault(c, {})
```
2. Easy travesal of Prefix Tree
```
    # Recursive
    def visit(node, word, prefix):
         if not word:
	    # Do sth.
         if '$' in node:
	    # Do sth.
	 c, w = word[0], word[1:] 
	 if c in node:
	    # Do sth.
	    visit(node[c], w, prefix+c)
```
Note prefix gives the visited characters in the Trie, `prefix+word` is the original input string within any recursion.

3. I realized that complicated problems need a CLEAN implementation of the Trie. Otherwise, the convenient implementation may cause confusions. As a programmer gets old, he/she should really put emphasis on the design and readability of a program, instead of the quick implementations.

**LC 336. Palindrome Pairs**

Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. `words[i] + words[j]` is a palindrome.

The idea is to use a Trie storing all the prefixes, a pair of strings `ab???` and `ba` matches, so you can reverse `ba` into `ab`, and search Trie to end up with some suffix `???`. If `???` is palindrome, then `ab???` and `ba` make a pair.

```
class TrieNode:
    def __init__(self):
        self.kids = {}
        self.end = -1
        self.pal = []
    
    # create the Trie, recording the index of a string in case of palindrome suffix
    def insert(self, i, s):
        if not s:
            self.end = i
        else:
            if s[::-1] == s:
                self.pal += i,
            if s[0] not in self.kids:
                self.kids[s[0]] = TrieNode()
            self.kids[s[0]].insert(i, s[1:])
    
    # search the Trie, collect the pairs of strings if concatenation is palindrome string
    def collect(self, i, s, ret):
        if not s:
            # Reach `ab?` with the input `ab`
            ret.extend([j, i] for j in self.pal)
            # Reach `ab` with the input `ab`
            if self.end not in [-1, i]:
                ret.append([self.end, i])
        else:
            # Reach `ab` with the input `abs`
            if self.end != -1 and s[::-1] == s:
                ret.append([self.end, i])
            if s[0] in self.kids:
                self.kids[s[0]].collect(i, s[1:], ret)
        
class Solution(object):
    def palindromePairs(self, words):
        root = TrieNode()
        for i, w in enumerate(words):
            root.insert(i, w)
        ret = []
        for i, w in enumerate(words):
            root.collect(i, w[::-1], ret)
        return ret
```
