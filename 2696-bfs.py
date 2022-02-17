from collections import deque
cnt=0
def bfs(graph,node,visited):
    global cnt
    queue=deque([node])
    visited[node]=True

    while queue:
        pop=queue.popleft()
        cnt+=1

        for i in graph[pop]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

n=int(input())
edge_num=int(input()) #컴퓨터가 연결되어 있는 수
edge=[]
for i in range(edge_num):
    edge_input=list(map(int,input().split()))
    edge.append(edge_input)

graph=[[] for i in range(n+1)]

for i in range(len(edge)):
    graph[edge[i][0]].append(edge[i][1])
    graph[edge[i][1]].append(edge[i][0])

visited=[False]*(n+1)
bfs(graph,1,visited)
print(cnt-1)