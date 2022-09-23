n=int(input())
food=list(map(int,input().split()))

#구현 편의를 위해 사용되는 인덱스 범위는 1~n으로 정함
#배열(리스트) 크기는 n+1로 잡음
dp=[0]*(n+1)
food.insert(0,0)

dp[1]=food[1]
dp[2]=max(food[1],food[2])

for i in range(3,n+1):
    dp[i]=max(dp[i-1],dp[i-2]+food[i])

print(dp[n])
