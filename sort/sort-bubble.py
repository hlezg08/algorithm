n=int(input())
arr=list(map(int,input().split()))

for i in range(len(arr)):
    for j in range(len(arr)-1-i):
        if(arr[j]>arr[j+1]): #오름차순 정렬
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)

