k,n=map(int,input().split())
lan=[]
for i in range(k):
    l=int(input())
    lan.append(l)

#이진 탐색 이용, 초기 end값은 랜선 길이 중 가장 긴 것 선택
start, end = 1, max(lan)

while start<=end:
    #mid=자를 길이
    mid=(start+end)//2
    cnt=0

    #랜선들을 mid 단위로 자름
    for l in lan:
        cnt+=l//mid

    #랜선 갯수를 모두 세서 목표 값(N)보다 크면 단위 길이를 늘려야 함
    #탐색 시작 값을 mid+1로 초기화
    if cnt>=n:
        start=mid+1
    #목표 값보다 작으면 단위 길이를 줄여서 N을 늘려야 함
    #탐색 끝 값을 mid-1로 초기화
    else:
        end=mid-1
        
#최종 값(end) 반환        
print(end)