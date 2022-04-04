testCaseCnt = int(input())
answer=[]
def solve (case,cur,curExp):
    
    
    if cur==case :
        curExp=curExp+str(cur)
        Exp=curExp.replace(" ","")
        if eval(Exp)==0:
            answer.append(curExp)
        return
    
    solve(case,cur+1,curExp+str(cur)+" ")
    solve(case,cur+1,curExp+str(cur)+"+")
    solve(case,cur+1,curExp+str(cur)+"-")
        
    
for i in range(testCaseCnt):
    case = int(input())
    solve(case,1,"")
    answer.append("")
    
for str in answer:
    print(str)

