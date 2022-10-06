from collections import deque
def solution(numbers, target):
    cnt=0
    queue=deque([numbers[0],-numbers[0]])
    i=0
    while queue:
        pop=queue.popleft()
        i+=1
        if i<len(numbers):
            queue.append(pop+numbers[i])
            queue.append(pop-numbers[i])
            
            print(queue)
        else:
            if pop==target: cnt+=1
    return cnt
            
