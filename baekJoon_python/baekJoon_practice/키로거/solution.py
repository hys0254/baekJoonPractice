caseCnt = int(input())
ans=[]
for i in range(caseCnt):
    testCase = list( input())
    tempAns=list()
    temp=list()
    for j in range(len(testCase)):
        if testCase[j]=="<":
            if not tempAns:
                continue
            temp.append(tempAns.pop())    
        elif testCase[j]==">":
            if not temp:
                continue
            tempAns.append(temp.pop())
        elif testCase[j]=="-":
            if not tempAns :
                continue
            tempAns.pop()
        else :
            tempAns.append(testCase[j])
    if temp :
        for j in range(len(temp)):
            tempAns.append(temp.pop())
    ans.append("".join(tempAns))
            
for i in ans:
    print(i)
            
        
        
    
    