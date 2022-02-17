def non_self_num(n):
	res=n
	while (n != 0):
		res += n % 10
		n=n//10
	return res

for i in range(1,10001):
    check = True	
    for j in range(1,10001):	
        if (i == non_self_num(j)):
            continue	
    
    if (check == True):
        print(i);
