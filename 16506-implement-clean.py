n=int(input())
assembly=[]
result=[]

op_list=['ADD','SUB','MOV','AND','OR','NOT','MULT',
'LSFTL','LSFTR','ASFTR','RL','RR']

for i in range(n):
    assembly.append(list(input().split()))

#기계어로 번역 시작
for op,d,a,b in assembly:
    tmp=''
    
    #0~4bit opcode를 번역
    #opcode를 리스트에 담아두었다가 입력에 들어오는 값이랑 비교, 해당 인덱스를 2진수로 변환
    for i in op_list:
        if(i in op):
            tmp+=format(op_list.index(i),'b').zfill(4)
    
    #만약 opcode 맨 뒤에 C가 붙어있을 경우
    if('C' in op):
        tmp+='1'
    else:
        tmp+='0'
    
    #5bit: 사용하지 않는 비트
    tmp+='0'

    #2진수로 변환, 원래 0b가 앞에 붙지만 format 함수를 이용해서 제거함
    rd=format(int(d),'b')

    #6~8bit: 3자리를 맞추기 위해 zfill 함수 사용
    tmp+=rd.zfill(3)

    #9~11bit: rA 중에서 상수 000으로 고정되는 경우와 나머지
    if('MOV' in op or 'NOT' in op):
        tmp+='000'
    else:
        ra=format(int(a),'b')
        tmp+=ra.zfill(3)
    
    #12~15bit: 4번 bit가 1일 경우 상수 #C로 고정됨
    if(tmp[4]=='1'):
        rc=format(int(b),'b')
        tmp+=rc.zfill(4)
    #그렇지 않으면 레지스터 rB 값
    else:
        rb=format(int(b),'b')
        tmp+=rb.zfill(3)
        tmp+='0'

    result.append(tmp)

for i in range(n):
    print(result[i])