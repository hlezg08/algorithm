from collections import deque
#구현 편의를 위해 graph, visited 배열 크기는 노드개수+1로 설정
#bfs 메서드 정의
def bfs(graph,start,visited):
    #1. 탐색 시작 노드를 큐에 삽입한 뒤 방문 처리
    queue=deque([start])
    visited[start]=True

    #2.큐에서 노드를 꺼낸 뒤 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
    while queue:
        pop=queue.popleft()
        print(pop,end=" ")

        for i in graph[pop]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
#각 노드가 연결된 정보 표현(2차원 리스트 이용)
#인접한 노드 모두 써야함
graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
#각 노드가 방문된 정보 표현
visited=[False]*9
#정의된 dfs 메서드 호출
bfs(graph,1,visited)