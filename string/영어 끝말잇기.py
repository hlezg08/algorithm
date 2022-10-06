def solution(n, words):
    answerIdx=0
    mentioned=[]
    passed=True
    
    for i in range(0,len(words)-1):
        if(words[i][-1]!=words[i+1][0]):
            passed=False
            answerIdx=i+1
            break
    
    for i in range(len(words)):    
        if(words[i] in mentioned):
            passed=False
            answerIdx=i
            break
        else:
            mentioned.append(words[i])
    
    return [0,0] if passed else [(answerIdx%n)+1,answerIdx//n+1]