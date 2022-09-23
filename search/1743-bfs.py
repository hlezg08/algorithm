from collections import deque

n,m,k=map(int,input().split())
trash=[]
for i in range(k):
    t=list(map(int,input().split()))
    trash.append(t)

matrix=[[0]*m for i in range(n)]
for i in range(len(trash)):
    matrix[trash[i][0]-1][trash[i][1]-1]=1

visited=[[False]*m for i in range(n)]
result=[]
dx=[0,0,-1,1]
dy=[-1,1,0,0]

for i in range(n):
    for j in range(m):
        
        if(matrix[i][j]==1 and not visited[i][j]):
            queue=deque([(i,j)])
            cnt=0
            
            while queue:
                x,y=queue.popleft() 
                for k in range(4):
                    nx=x+dx[k]
                    ny=y+dy[k]

                    if 0<=nx<n and 0<=ny<m:
                        if not visited[nx][ny] and matrix[nx][ny]==1:
                            visited[nx][ny]=True
                            cnt+=1
                            queue.append((nx,ny))
                          
            result.append(cnt)
        
print(result)
