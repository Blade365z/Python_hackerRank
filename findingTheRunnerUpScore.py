def runnerup(score):
    winner = max(score)
    runnerUp = []
    for i in score : 
        if(i!=winner):
            runnerUp.append(i)
        
    runnerUp= max(runnerUp)
    print(runnerUp)

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    marks = []
    for i in arr:
        marks.append(i)
    runnerup(marks)
