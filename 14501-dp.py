n=int(input())
t=[]
p=[]
dp=[0]*(n+1)

for i in range(n):
    a,b=map(int,input().split())
    t.append(a)
    p.append(b)

#금액이 상담 끝나는 날 받을 수 있으므로 마지막날 부터 하루씩 감소
for i in range(n-1,-1,-1):
    if(i+t[i]>n):#현재 일차와 상담 소요 시간을 더했을 때 n보다 큰 경우(상담 못함)
        dp[i]=dp[i+1] #이전 날짜의 금액 그대로
    else:
        dp[i]=max(dp[i+1],p[i]+dp[i+t[i]])
        #dp[i+t[i]]+p[i]는 i일차에 상담을 했을 경우 예상되는 금액
        #dp[i+1]은 i일차는 하지 않고 그 이전 날짜 금액 그대로

print(dp[0])