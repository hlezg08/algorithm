from collections import deque
vertexList = ['0', '1', '2', '3', '4', '5', '6']
edgeList = [(0,1), (0,2), (1,3),
 (2,4),(2,5), (4,6)]
#undirected의 경우 양쪽 방향을 다 넣고 directed의 경우 한방향만 리스트에 넣으면 됨

graphs = (vertexList, edgeList)

def bfs(graph, root):
    vertexList, edgeList = graph
    visitedList = []
    queue = deque([root])
    adjacencyList = [[] for vertex in vertexList] #인접 리스트 초기화

    # fill adjacencyList from graph
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    # bfs
    while queue:
        current = queue.popleft()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedList:
                queue.append(neighbor)
        visitedList.append(current)
    return visitedList

print(bfs(graphs, 0))