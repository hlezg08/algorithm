from itertools import permutations
def solution(numbers):
    numbers=list(map(lambda x:str(x),numbers))
    arr=list(permutations(numbers,len(numbers)))
    results=[]
    for num in arr:
        num=''.join(num)
        results.append(int(num))
    return str(max(results))