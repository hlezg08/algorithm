from collections import deque

def solution(priorities, location):
    result=[]
    queue=deque([])
    
    for i in range(0,len(priorities)):
        queue.append([i,priorities[i]])
    
    while(True):
        temp=queue.popleft()
        passed=True
        
        for wait in queue:
            if(temp[1]<wait[1]):
                passed=False
                queue.append(temp)
                break
            
        if(passed): 
            result.append(temp)
        if(len(queue)==0):
            break
    
    for arr in result:
        if(location==arr[0]):
            return result.index(arr)+1