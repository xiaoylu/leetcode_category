class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=b=c=0
        ug=[1]
        while len(ug)<n:
            x,y,z = 2*ug[a],3*ug[b],5*ug[c]
            m = min(x,y,z)
            if m==x: a+=1
            if m==y: b+=1
            if m==z: c+=1
            ug.append(m)
        return ug[-1]
