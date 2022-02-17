n,k=map(int,input().split())
country=[[] for i in range(n)]
for i in range(n):
    country[i]=list(map(int,input().split()))

#버블정렬 이용
for j in range(n-1,0,-1):
    for i in range(j):
        if(country[i][1]<country[i+1][1]):
            country[i],country[i+1]=country[i+1],country[i]
        elif(country[i][1]==country[i+1][1] and country[i][2]<country[i+1][2]):
            country[i],country[i+1]=country[i+1],country[i]
        elif(country[i][1]==country[i+1][1] and country[i][2]==country[i+1][2] and country[i][3]<country[i+1][3]):
            country[i],country[i+1]=country[i+1],country[i]  

rank=1
for i in range(n):
    if(country[i][0]==k):
        index=i

for j in range(index):
    if(country[j][1]==country[index][1] and country[j][2]==country[index][2] and country[j][3]==country[index][3]):
        continue
    else:
        rank+=1

print(rank)