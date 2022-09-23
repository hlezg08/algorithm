vertexList = ['0', '1', '2', '3', '4', '5', '6']
edgeList = [(0,1), (0,2), (1,0), (2,0),(1,3),(3,1),
 (2,4),(4,2) ,(2,5),(5,2), (4,6),(6,4)]
#undirected의 경우 양쪽 방향을 다 넣고 directed의 경우 한방향만 리스트에 넣으면 됨

graphs = (vertexList, edgeList)

def bfs(graph, root):
    vertexList, edgeList = graph
    visitedList = []
    queue = [root]
    adjacencyMatrix = [[0]*len(vertexList)  for i in range(len(vertexList))]
    
    # fill adjacencyList from graph
    for edge in edgeList:
        adjacencyMatrix[edge[0]][edge[1]]=1

    # bfs
    while queue:
        current = queue.pop()
        for i in range(len(adjacencyMatrix[current])):
            if(adjacencyMatrix[current][i]==1 and current not in visitedList):
                queue.append(i)
        visitedList.append(current)
    return visitedList
    

print(bfs(graphs, 0))