def find_parent(parent,node):
    if(parent[node]!=node):
        # return 빼먹음
        return find_parent(parent,parent[node])
    return node

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
        
    #print('parent',parent[a],parent[b])
    
v,e=map(int,input().split())
parent=[0]*(v)

for i in range(v):
    parent[i]=i

for i in range(e):
    a,b=map(int,input().split())
    union_parent(parent,a,b)

print('각 원소가 속한 집합: ',end='')
for i in range(v):
    print(find_parent(parent,i),end='')
    
print()
print(parent)