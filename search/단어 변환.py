from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue=deque()
    queue.append([begin,0])
    visited=[0 for _ in range(len(words))]
    answer=0
    
    while queue:
        word,depth=queue.popleft()
        
        if(word==target):
            answer=depth
            return answer
        
        for i in range(len(words)):
            diff_cnt=0
            
            for j in range(len(words[i])):
                if(words[i][j]!=word[j]):
                    diff_cnt+=1
                
            if(diff_cnt==1 and visited[i]==0):
                queue.append([words[i],depth+1])
                visited[i]=1