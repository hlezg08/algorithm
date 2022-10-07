def dfs(graph,index,visited):
    visited[index]=True

    for node in range(len(graph)):
        if graph[index][node]==1 and visited[node]==False:
            dfs(graph,node,visited)

def solution(n,computers):
    answer=0
    visited=[False]*n
    for i in range(n):
        if visited[i]==False:
            dfs(computers,i,visited)
            answer+=1
    return answer