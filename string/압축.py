def solution(msg):
    result=[]
    word=[0]
    for i in range(26):
        word.append(chr(ord('A')+i))
        
    w,c=0,0
    
    while(True):
        c+=1
        if(c==len(msg)):
            result.append(word.index(msg[w:c]))
            break
        if(msg[w:c+1] not in word):
            word.append(msg[w:c+1])
            result.append(word.index(msg[w:c]))
            w=c
    
    return result