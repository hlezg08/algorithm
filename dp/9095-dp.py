t=int(input())
for i in range(t):
    n=int(input())
    dp=[0]*(n+1)

    dp[0]=1
    dp[1]=1
    
    if n>=2:
        dp[2]=2

    if n>=3:
        for i in range(3,n+1):
            dp[i]=dp[i-3]+dp[i-2]+dp[i-1]

    print(dp[n])