from collections import deque

n,m=map(int,input().split())
miro=[]

for i in range(n):
    miro.append(list(input()))

queue=deque([(0,0)])
visited=[[0]*m for i in range(n)]

#방향 L,R,U,D 순
dx=[0,0,-1,1]
dy=[-1,1,0,0]

#1. 탐색 시작 노드를 큐에 삽입한 뒤 방문 처리
visited[0][0]=1

#2.큐에서 노드를 꺼낸 뒤 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
while queue:
    x,y=queue.popleft()
    
    if x==n-1 and y==m-1:
        print(visited[x][y])
        break

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<m: #배열 범위 안 
            if visited[nx][ny]==0 and miro[nx][ny]=='1':
                visited[nx][ny]=visited[x][y]+1
                queue.append((nx,ny))