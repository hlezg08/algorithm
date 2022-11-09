
graph=[[1,1,0,0,0], [1,1,0,0,0], [0,0,0,0,0], [0,0,0,1,1]]
n,m=len(graph),len(graph[0])


visited=[]

def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m: return False
    if [x,y] not in visited and graph[x][y]==1:
        visited.append([x,y])
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1
            
print(result)
                


    