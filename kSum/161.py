class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = len(s) - len(t)
        for i, (a, b) in enumerate(zip(s,t)):
            if a != b:
                return s[i+(d>=0):]==t[i+(d<=0):]
        return abs(d)==1
