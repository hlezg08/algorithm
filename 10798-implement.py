list=[]
for i in range(5):
    sentence=input()
    list.append(sentence)

result=""
max_length=max([len(list[i]) for i in range(5)])

for i in range(max_length):
    for j in range(5):
        if len(list[j])<i+1:
            continue
        else:
            result=result+list[j][i]

print(result)
