#재귀로 하면 메모리 초과, 반복문(bottom up)으로 하니 정답
n=int(input())
d=[]
for i in range(n+1):
    d.append(0)

d[1]=0

for i in range(2,n+1):
    d[i]=d[i-1]+1
    if(i%2==0 and (d[i]>d[i//2]+1)):
        d[i]=d[i//2]+1
    if(i%3==0 and (d[i]>d[i//3]+1)):
        d[i]=d[i//3]+1

print(d[n])
