import sys
testCaseCnt=int(sys.stdin.readline())

zeroList=[1,0,1]
oneList=[0,1,1]
ans=list()

def pibo(num):
    length=len(zeroList)
    if length<=num :
        for i in range(length,num+1):
            zeroList.append(zeroList[i-1]+zeroList[i-2])
            oneList.append(oneList[i-1]+oneList[i-2])
        

for _ in range(testCaseCnt):
    
    temp=int(sys.stdin.readline())
    ans.append(temp)
    pibo(temp)

    
for i in ans:
    print(zeroList[i],oneList[i])
    
    