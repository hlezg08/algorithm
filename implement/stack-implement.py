class Stack:
    def __init__(self):
        self.items=[]
    
    def push(self,value):
        self.items.append(value)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            return -1

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            return -1

    def isEmpty(self):
        if (len(self.items)==0):
            return True
        else:
            return False
