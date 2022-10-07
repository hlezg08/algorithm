import sys
input=sys.stdin.readline

computer_num=int(input())
edge_num=int(input()) 
edge=[]

for i in range(edge_num):
    edge_input=list(map(int,input().split()))
    edge.append(edge_input)

def dfs(graph,idx,visited):
    visited[idx]=True

    for node in graph[idx]:
        if not visited[node]:
            dfs(graph,node,visited)
    
def solution(computer_num,edge):
    graph=[[] for _ in range(computer_num+1)]
    for arr in edge:
        graph[arr[0]].append(arr[1])
        graph[arr[1]].append(arr[0])
    
    visited=[False]*(computer_num+1)
    dfs(graph,1,visited)
    
    visited=visited[1:]
    return visited.count(True)-1

print(solution(computer_num,edge))

