from collections import deque
def solution(numbers, target):
    cnt=0
    queue=deque([[numbers[0],0],[-numbers[0],0]])
    idx=0
    while queue:
        pop,idx=queue.popleft()
        idx+=1
        if idx<len(numbers):
            queue.append([pop+numbers[idx],idx])
            queue.append([pop-numbers[idx],idx])
        else:
            if pop==target: cnt+=1
    return cnt
            
