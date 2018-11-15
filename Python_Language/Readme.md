Python 
===

MRO (Method Resolution Order)
---
The class C inherits class A and B. 

If both A and B define the same parameter `val`, 
a risk is that both A and B's `__init__` modifies this `val` in an unknown order.

The `super` method makes sure only one copy of `val` is preserved, 
but it needs a MRO to determine eventually which class's method gets called.

```
#    Base
#   /    \ 
#  A      B
#   \    /
#      C
# every class defines a variable val

class C(A, B):
    def show(self):
        print(self.val)
        
    def __init__(self, val):
        super(C, self).__init__(val)
```
