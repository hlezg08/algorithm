size=int(input())
tri=[]
for i in range(size):
    num=list(map(int,input().split()))
    tri.append(num)

for i in range(1,size):
    for j in range(i+1):
        if(j==0):
            tri[i][0]+=tri[i-1][0]
        elif(j==i):
            tri[i][j]+=tri[i-1][j-1]
        else:
            tri[i][j]+=max(tri[i-1][j],tri[i-1][j-1])

print(max(tri[size-1]))