numCnt = int(input())
numList=[]
for i in range(numCnt):
    numList.append(int(input()))
numList.sort()
for i in numList:
    print(i)