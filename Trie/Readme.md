## Notes
1. Easy creation of Prefix Tree
```
    node = self.root
    for c in word+"$":
        node = node.setdefault(c, {})
```
