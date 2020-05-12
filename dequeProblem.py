from collections import deque
n = int(input())
d=deque()
for i in range(n):
    inputU=input()
    if ' ' not in inputU:
            func = inputU
    else:
        func,value=inputU.split()
        value=int(value)
    if(func=='append'):
        d.append(value)
    elif(func=='appendleft'):
        d.appendleft(value)
    elif(func=='pop'):
        d.pop()
    elif(func=='popleft'):
        d.popleft()
        
for i in d :
     print (i , end=" ")
