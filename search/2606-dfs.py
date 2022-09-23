#입력으로 들어온 컴퓨터 번호 쌍을 연결리스트로 바꾼 뒤 dfs 실행
cnt=0
def dfs(graph,node,visited):
    global cnt
    visited[node]=True
    cnt+=1
    for i in graph[node]:
        if not visited[i]:
            dfs(graph,i,visited)
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
dfs(graph,1,visited)
print(cnt-1)