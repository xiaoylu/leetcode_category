# Stack

## Parentheses Problems

## Tree

For tree problems, stack can be used to convert recursons to iterations.
On the other hand, you can also use deque for the same purpose.

```
    def closestKValues(self, root, target, k):
#      *
#      4
#    /   \
#   2     5
#  / \  
# 1   3
#      \
#       3.9
# lQ = 1, 2, 3 
# rQ = 3.9, 4, 5
        lQ, rQ = deque(), deque()
        self.inorder(root, target, lQ, rQ)
        res = []
        while len(res) < k and (lQ or rQ):
            if not rQ: res.append(lQ.pop())
            elif not lQ: res.append(rQ.popleft())
            else:    
                if abs(lQ[-1] - target) < abs(rQ[0] - target):
                    res.append(lQ.pop())
                else:
                    res.append(rQ.popleft())
        return res

    def inorder(self, root, V, lQ, rQ):
        if not root: return
        self.inorder(root.left, V, lQ, rQ)
        
        if (V < root.val): rQ.append(root.val)
        else: lQ.append(root.val)
        
        self. inorder(root.right, V, lQ, rQ)
```
