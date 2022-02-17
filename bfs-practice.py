from collections import deque

def BFS(graph,root):
    visited=[]
    queue=deque([root]) #큐 초기화(root node가 들어감)

    while(queue): #while(queue)로도 가능
        n=queue.popleft() #숫자를 꺼낸다
        if n not in visited: #방문한 적 없는 숫자의 경우
            visited.append(n) #visited에 집어넣고(출력)
            queue+=graph[n]-set(visited) #n과 인접한 노드들을 큐에 집어넣는다
    return visited

#directed graph
graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}

root_node = 1

print(BFS(graph_list,root_node))