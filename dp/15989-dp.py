t=int(input())
dp=[1]*(10000+1)#어떤 숫자던지 방법은 1가지 이상 가지고 있으므로 1로 초기화

for i in range(2,10001): #2를 더하는 경우
    dp[i]+=dp[i-2]
    
for i in range(3,10001): #3을 더하는 경우
    dp[i]+=dp[i-3]

for _ in range(t):
    n=int(input())
    print(dp[n])