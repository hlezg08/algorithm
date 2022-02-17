n=int(input())
cnt=0

#':' 문자열을 굳이 포함할 필요 없음
for i in range(n+1): #시(0~n까지)
    for j in range(60): #분
        for k in range(60): #초
            if('3' in str(i)+str(j)+str(k)): #3이 하나라도 해당되면 카운트+1
                cnt+=1
print(cnt)