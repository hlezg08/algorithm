n1,n2=map(int,input().split())

group1=input()
group2=input()
t=int(input())

group1=group1[::-1]
result=group1+group2
result=list(result) #문자열은 인덱스 교환이 안되므로 리스트 형태로 변환

for _ in range(t):
    tmp_idx=[]
    for i in range(len(result)-1):
        if(result[i] in group1 and result[i+1] in group2):
            tmp_idx.append(i)

    for idx in tmp_idx:
        result[idx],result[idx+1]=result[idx+1],result[idx]

final=""
for i in result:
    final+=i

print(final)