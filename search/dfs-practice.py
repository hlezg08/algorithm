import sys
from collections import deque

vertexList = ['0', '1', '2', '3', '4', '5', '6']
edgeList = [(0,1), (0,2), (1,3),(2,4),(2,5), (4,6)]
graphs=vertexList,edgeList

def DFS(graph,root):
    vertexList,edgeList=graph
    visitedList=[]
    stack=[root]
    
    adjacencyList = [[] for vertex in vertexList]

    # fill adjacencyList from graph
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])
    
    while stack:
        current = stack.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedList:
                stack.append(neighbor)
        visitedList.append(current)
    return visitedList

print(DFS(graphs,0))
