class Queue:
    def __init__(self):
        self.items=[]

    def push(self,val):
        self.items.append(val)
    
    def pop(self):
        front=0
        if(self.empty()==0):
            front=self.items[0]
            self.items=self.items[1:]
            return front
        else: 
            return -1

    def empty(self):
        if(len(self.items)==0):
            return 1
        else:
            return 0

import sys

q=Queue()
n=int(input())

for i in range(n):
    command=sys.stdin.readline().split()

    if(command[0]=='push'):
        q.push(command[1])
        
    elif(command[0]=='pop'):
        print(q.pop())

    elif(command[0]=='size'):
        print(len(q.items))

    elif(command[0]=='empty'):
        print(q.empty())

    elif(command[0]=='front'):
        if(q.empty()==1):
            print(-1)
        else:
            print(q.items[0]) 

    elif(command[0]=='back'):
        if(q.empty()==1):
            print(-1)
        else:
            print(q.items[-1]) 
