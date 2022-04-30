testCaseCnt = int(input())
ans=[]
for i in range(testCaseCnt):
    paperCnt, target = list(map(int,input().split(' ')))
    paperList= list(map(int,input().split(' ')))
    paperList = [(i,idx)for idx,i in enumerate(paperList)]
    count =0
    while True:
        if paperList[0][0]== max(paperList,key=lambda x:x[0])[0]:
            count+=1
            if paperList[0][1]==target:
                ans.append(count)
                break
            else :
                paperList.pop(0)       
        else :
            paperList.append(paperList.pop(0))
    
for answer in ans :
    print(answer)
                      
    