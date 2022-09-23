n=int(input())
directions=input().split()
x,y=1,1 #처음 위치 1,1로 초기화

#L,R,U,D 순으로 x,y방향 좌표 설정
dx=[0,0,-1,1]
dy=[-1,1,0,0]
types=['L','R','U','D']

for dir in directions:
    for i in range(len(types)):
        if dir==types[i]: #입력으로 들어온 방향이 L,R,U,D에 해당될 때
            nx=x+dx[i] #x좌표(행) 방향을 더함
            ny=y+dy[i] #y좌표(열)도 x와 똑같이
    if nx>n or ny>n or nx<1 or ny<1: #nxn 영역을 벗어나면 좌표를 더하지 않고 건너뜀
        continue
    x,y=nx,ny #여러번 좌표를 더한 최종 값을 x와 y에 대입

print(x,y)