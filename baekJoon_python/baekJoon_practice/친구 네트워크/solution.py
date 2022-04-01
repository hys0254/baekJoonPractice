def find(x):
    if x==parentList[x] :
        return x
    else:
        p=find(parentList[x])
        parentList[x]=p
        return parentList[x]
    
def union(x,y):
    x=find(x)
    y=find(y)
    if x!=y :
        parentList[y]=x
        countList[x]+=countList[y]
            


testCaseCnt =int(input())
ans =list()
for i in range (testCaseCnt):
    caseCnt = int(input())
    parentList =dict()
    countList=dict()
    for j in range(caseCnt) :
        tempList = input().split(" ")
        if tempList[0] not in parentList:
            parentList[tempList[0]]=tempList[0]
            countList[tempList[0]]=1
        if tempList[1] not in parentList:
            parentList[tempList[1]]=tempList[1]
            countList[tempList[1]]=1
            
        union(tempList[0],tempList[1])
        
        ans.append(countList[find(tempList[0])])

for i in ans:
    print(i)

