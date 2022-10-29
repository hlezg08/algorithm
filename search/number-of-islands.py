class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
      
        result=0
        
        def dfs(x,y):
            if x<0 or x>=n or y<0 or y>=m: return False
            # 방문여부를 나타내는 배열(visited)을 만들어서 시간초과 발생
            # visited 만들지 않고도 육지('1')가 있는지 확인하고
            # '0'으로 바꿔주면 다음에 다시 탐색할 필요가 없다
            if grid[x][y]=='1':
                grid[x][y]='0'
                dfs(x-1,y)
                dfs(x+1,y)
                dfs(x,y-1)
                dfs(x,y+1)
                return True
            return False

        for i in range(n):
            for j in range(m):
                if dfs(i,j):
                    result+=1

        return result
            
        