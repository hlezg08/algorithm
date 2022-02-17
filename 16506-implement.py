n=int(input())
assembly=[]
result=[]
for i in range(n):
    assembly.append(list(input().split()))

for i in range(n):
    tmp=''
    if(assembly[i][0]=='ADD' or assembly[i][0]=='ADDC'):
        tmp+='0000'
    if(assembly[i][0]=='SUB' or assembly[i][0]=='SUBC'):
        tmp+='0001'
    if(assembly[i][0]=='MOV' or assembly[i][0]=='MOVC'):
        tmp+='0010'
    if(assembly[i][0]=='AND' or assembly[i][0]=='ANDC'):
        tmp+='0011'
    if(assembly[i][0]=='OR' or assembly[i][0]=='ORC'):
        tmp+='0100'
    if(assembly[i][0]=='NOT'):
        tmp+='0101'
    if(assembly[i][0]=='MULT' or assembly[i][0]=='MULTC'):
        tmp+='0110'
    if(assembly[i][0]=='LSFTL' or assembly[i][0]=='LSFTLC'):
        tmp+='0111'
    if(assembly[i][0]=='LSFTR' or assembly[i][0]=='LSFTRC'):
        tmp+='1000'
    if(assembly[i][0]=='ASFTR' or assembly[i][0]=='ASFTRC'):
        tmp+='1001'
    if(assembly[i][0]=='RL' or assembly[i][0]=='RLC'):
        tmp+='1010'
    if(assembly[i][0]=='RR' or assembly[i][0]=='RRC'):
        tmp+='1011'

    if('C' in assembly[i][0]):
        tmp+='1'
    else:
        tmp+='0'
    
    tmp+='0'
    #2진수로 변환, 원래 0b가 앞에 붙지만 format 함수를 이용해서 제거함
    rd=format(int(assembly[i][1]),'b')
    #6~8bit: 3자리를 맞추기 위해 zfill 함수 사용
    tmp+=rd.zfill(3)

    if('MOV' in assembly[i][0] or 'NOT' in assembly[i][0]):
        tmp+='000'
    else:
        ra=format(int(assembly[i][2]),'b')
        tmp+=ra.zfill(3)
    
    if(tmp[4]=='1'):
        rc=format(int(assembly[i][3]),'b')
        tmp+=rc.zfill(4)
    else:
        rb=format(int(assembly[i][3]),'b')
        tmp+=rb.zfill(3)
        tmp+='0'

    result.append(tmp)

for i in range(n):
    print(result[i])