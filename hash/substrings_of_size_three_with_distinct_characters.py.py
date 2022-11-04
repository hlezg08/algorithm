class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        substrings=[]
        answer=[]
        for i in range(len(s)-2):
            substrings.append(s[i:i+3])
        
        for string in substrings:
            cnt={}
            passed=True
            
            for i in range(len(string)):
                if string[i] not in cnt:
                    cnt[string[i]]=1
                else:
                    cnt[string[i]]+=1
                    
            for key,value in cnt.items():
                if(value>=2):
                    passed=False
            if(passed): answer.append(string)
                
        return len(answer)