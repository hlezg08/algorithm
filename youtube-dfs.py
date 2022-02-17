#구현 편의를 위해 graph, visited 배열 크기는 노드개수+1로 설정
#dfs 메서드 정의,재귀 호출 이용
def dfs(graph,node,visited):
    visited[node]=True
    print(node,end=' ')

    for i in graph[node]:
        if not visited[i]: ##'==False'와 같은 의미
            dfs(graph,i,visited)
#각 노드가 연결된 정보 표현(2차원 리스트 이용)
#인접한 노드 모두 써야함
graph=[
    [],
    [2,5],
    [1,3,5],
    [2],
    [7],
    [1,2,6],
    [5],
    [4],
]
#각 노드가 방문된 정보 표현
visited=[False]*9
#정의된 dfs 메서드 호출
dfs(graph,1,visited)