memberCnt = int(input())
memberList = list()
for i in range(memberCnt):
    tempList = input().split(' ')
    memberList.append((int(tempList[0]),tempList[1]))
memberList.sort(key=lambda x:x[0])
for member in memberList:
    print(member[0],member[1])