import sys
houseCnt, routerCnt = map(int, input().split())
houseList=[]
for _ in range(houseCnt):
    houseList.append(int(sys.stdin.readline()))
houseList.sort()
min=1000000001
for i in range(len(houseList)-1):
    if abs(houseList[i]-houseList[i+1])<min:
        min=abs(houseList[i]-houseList[i+1])
max=houseList[-1]-houseList[0]
result=0

while min<=max:
    mid = (min+max)//2
    curHousePos = houseList[0]
    count=1
    for i in range(1,len(houseList)):
        if houseList[i]>=curHousePos+mid:
            count+=1
            curHousePos=houseList[i]
    if count>=routerCnt:
        min=mid+1
        result=mid
    else:
        max=mid-1
       

print(result)
 
 
 
