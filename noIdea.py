n,m=input().split()
array= list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = 0 
for  i in array :
     if i in a:
            result = result +1 
     if i in b:
            result = result -1
            
print(result)
