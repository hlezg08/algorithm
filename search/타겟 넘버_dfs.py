cnt=0
def dfs(numbers,sum,idx,target):
    global cnt
    if idx==len(numbers):
        if sum==target:
            cnt+=1
        return
    else:
        dfs(numbers,sum+numbers[idx],idx+1,target)
        dfs(numbers,sum-numbers[idx],idx+1,target)
    
def solution(numbers, target):
    dfs(numbers,0,0,target)
    return cnt
