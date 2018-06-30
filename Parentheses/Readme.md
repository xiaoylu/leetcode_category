# The parentheses problem is essentially stack problem.

**LC 301. Remove Invalid Parentheses**
```
    def removeInvalidParentheses(self, s):
        # when you have one extra ")", remove it
        # caution: remove the ")" after the position of last removal to avoid duplicates
        def fix(s, start, last_removal):
            counter = 0
            for i in range(start, len(s)):
                if s[i]==')': counter -= 1
                elif s[i]=='(': counter += 1
                if counter < 0: # fix    
                    ret = []
                    for j in range(last_removal, i+1):
                        if s[j]==')' and (j==0 or s[j-1] != s[j]):
                            ret += fix(s[:j]+s[j+1:], i, j)
                    return ret
            return [s]
            
        # (() => )(( => ()) 
        def reverse(s):
            ss = ""
            for c in s[::-1]:
                if '('==c: ss += ")"
                elif ')'==c: ss += "("
                else: ss += c 
            return ss
        
        right = fix(s, 0, 0)
        left = []
        for s in right:
            left += fix(reverse(s),0,0)
        return [reverse(s) for s in left]
```
