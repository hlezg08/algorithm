class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
       
        count=0
        def dfs(x,y):
            if(x<0 or x>=n or y<0 or y>=m): return
            if(grid[x][y]==0): return
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)
            count+=1
            return count
            
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==1):
                    print(dfs(i,j))