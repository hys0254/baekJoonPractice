cordCnt = int(input())
cordList =list()
for _ in range(cordCnt):
    x,y =map(int,input().split(' '))
    cordList.append((x,y))
    
cordList.sort(key=lambda x:(x[0],x[1]))

for i in range(cordCnt):
    print(cordList[i][0],cordList[i][1])