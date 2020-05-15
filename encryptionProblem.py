import math
s  = input()
sLength=len(s)
x,y=math.floor(math.sqrt(sLength)),math.ceil(math.sqrt(sLength))
if(x*y<sLength):
    while(x*y<=sLength and x<=y):
            x=x+1
    row=x
    col=y
    
else:
    row=x
    col=y


for i in range(col):
        index=0
        for flag in range(row):
            index=i+y*flag
            if(index<sLength):
                print(s[i+y*flag],end="")
        print(" ",end="")
