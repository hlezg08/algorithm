from collections import deque
test_num=int(input())
for i in range(test_num):
    N,M=map(int,input().split())
    queue=deque(list(map(int,input().split())))
    index=deque([i for i in range(N)])

    cnt=0
    while queue:
        if(queue[0]==max(queue)):
            cnt+=1
            queue.popleft()
            if(index.popleft()==M):
                print(cnt)
        else:
            queue.append(queue.popleft())
            index.append(index.popleft())
        

