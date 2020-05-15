q = int(input())
mainArray = []
array=[]
for j in range(q):
    n = int(input())
    for i in range(n):
        array.append(list(map(int, input().split())))
    mainArray.append(array)
    array=[]
for element in mainArray:
    sumel=[]
    sumcol= []
    counter=0
    sumflag=0
    k=0
    sumcol=[sum(x) for x in zip(*element)]
    for i in element:
        sumel.append(sum(i))
        
    if(set(sumel)==set(sumcol)):
        print('Possible')
    else:
        print('Impossible')
        
