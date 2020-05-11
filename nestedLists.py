if __name__ == '__main__':
    marks= {}
    scores=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marks[name]=score
        scores.append(score)
    x=min(scores)
    sorted_list={}
    sorted_list= {key:value for key, value in marks.items() if value!=x }
    sorted_x =  min(sorted_list.items(), key=lambda x: x[1]) 
    runnerUp={key:value for key,value in sorted_list.items() if value==sorted_x[1]}
    for k,v in sorted(runnerUp.items()):
        print (k)
   
