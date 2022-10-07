def solution(dp):
    n=len(dp)
    for i in range(1,n):
        for j in range(0,i+1):
            if j==0:
                dp[i][j]+=dp[i-1][0]
            elif j==i:
                dp[i][j]+=dp[i-1][i-1]
            else:
                dp[i][j]+=max(dp[i-1][j-1],dp[i-1][j])
    return max(dp[n-1])