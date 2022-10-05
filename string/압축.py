def solution(msg):
    result=[]
    word=[0]
    for i in range(26):
        word.append(chr(ord('A')+i))
        
    for i in range(len(msg)):
        temp=msg[i]
        for j in range(i,len(msg)):
            if(temp not in word):
                word.append(temp)
                result.append(word.index(temp[0:-1]))
                break
            else:
                if(j+1<=len(msg)-1):
                    temp+=msg[j+1]
                
                
    print(word)