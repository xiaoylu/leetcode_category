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
