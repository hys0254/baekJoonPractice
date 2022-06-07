import sys
numCnt = int(sys.stdin.readline())
numDict=dict()
for _ in range(numCnt):
    temp=int(sys.stdin.readline())
    numDict[temp]=numDict.get(temp,0)+1
    


for i in range(1,10001):
    if numDict.get(i,0)==0:
        continue
    for j in range(numDict[i]):
        print(i)