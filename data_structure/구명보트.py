from collections import deque
def solution(people, limit):
    answer=[]
    people.sort()
    people=deque(people)
    
    while(len(people)>0):
        front=people.popleft()
        if(len(people)==0):
            answer.append([front])
            break
        last=people.pop()
        
        if(front+last<=limit):
            answer.append([front,last])
        else:
            answer.append([front])
            people.appendleft(front)
    
    return len(answer)