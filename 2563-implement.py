n=int(input())
paper=[[0 for _ in range(101)] for i in range(101)]

#처음에는 100*색종이의 수-겹치는 영역의 넓이 계산하는 방법 생각
#겹치는 영역의 넓이 구하는 것이 비효율적이라고 느낌
for i in range(n):
    a,b=input().split()
    a=int(a)
    b=int(b)
    for i in range(10):
        for j in range(10):
            paper[a+i][b+j]=1
sum=0
for i in range(101):
    for j in range(101):
        sum+=paper[i][j]

print(sum)



