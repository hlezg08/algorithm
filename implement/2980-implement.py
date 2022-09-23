#문제 이해하는 것부터 막힘..
n,l=map(int,input().split())
time=0
current=0

for i in range(n):
    d,r,g=map(int,input().split())

    time+=(d-current)
    current=d

    #파란불이면 바로 가도 되므로 빨간불일 때만 생각
    if(time%(r+g)<=r):
        time+=(r-time%(r+g))

time+=(l-current)
print(time)