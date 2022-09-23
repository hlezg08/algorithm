n=int(input())
dp=[0]*(n+1)

dp[1]=0

for i in range(2,n+1):
    #1을 빼거나 나눗셈 연산을 1번 수행 하므로 모두 경우에 1 더함
    #1을 빼는 경우
    dp[i]=dp[i-1]+1
    #3으로 나누어 떨어질 때 원래 값과 dp[i//3]값 비교
    if(i%3==0):
        dp[i]=min(dp[i],dp[i//3]+1)
    #2로 나누어 떨어질 때 원래 값과 dp[i//2]값 비교
    if(i%2==0):
        dp[i]=min(dp[i],dp[i//2]+1)

print(dp[n])
        