class Solution:
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        ret = 0
        swap = [1]*len(A)
        noswap = [0]*len(A)
        for i in range(1,len(A)):
            x = noswap[i-1]+1 if A[i]>B[i-1] and B[i]>A[i-1] else len(A)+1
            y = swap[i-1]+1 if A[i]>A[i-1] and B[i]>B[i-1] else len(A)+1
            swap[i] = min(x, y)
            print(i,".",swap[i])
            x = noswap[i-1] if A[i]>A[i-1] and B[i]>B[i-1] else len(A)+1
            y = swap[i-1] if A[i]>B[i-1] and B[i]>A[i-1] else len(A)+1
            noswap[i] = min(x, y)
            print(i,".",noswap[i])
        return min(swap[len(A)-1],noswap[len(A)-1])

print( Solution().minSwap([0,3,5,8,9],[2,1,4,6,9]) )
