class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        grid = [[N] * N for i in range(N)]
        for m in mines:
            grid[m[0]][m[1]] = 0
        for i in range(N):
            l,r,u,d=0,0,0,0
            for j in range(N):
                k = N-j-1
                l = l+1 if grid[i][j]!=0 else 0
                grid[i][j] = min(grid[i][j],l)
                
                r = r+1 if grid[i][k]!=0 else 0
                grid[i][k] = min(grid[i][k],r)
                
                u = u+1 if grid[j][i]!=0 else 0
                grid[j][i] = min(grid[j][i],u)
                
                d = d+1 if grid[k][i]!=0 else 0
                grid[k][i] = min(grid[k][i],d)                
        return max([max(grid[i]) for i in range(N)])
