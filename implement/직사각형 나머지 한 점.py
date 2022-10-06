def solution(v):
    x={}
    y={}
    
    result=[]
    
    for arr in v:
        if arr[0] not in x:
            x[arr[0]]=1
        else:
            x[arr[0]]+=1
        if arr[1] not in y:
            y[arr[1]]=1
        else:
            y[arr[1]]+=1
    
    for key,value in x.items():
        if value==1:
            result.append(key)
            
    for key,value in y.items():
        if value==1:
            result.append(key)
            
    return result