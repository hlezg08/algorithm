import math
def solution(n, m):
    gcd_num=math.gcd(n,m)
    return [gcd_num,n*m//gcd_num]