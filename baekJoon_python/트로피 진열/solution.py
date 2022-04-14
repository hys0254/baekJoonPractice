


trophyCnt = int(input())
trophyList =[]
ans=[]
for _ in range(trophyCnt):
    trophyList.append(int(input()))
stack = []
for i ,trophy in enumerate(trophyList):
    if i==0:
        stack.append(trophy)
        continue
    if stack[-1]<trophy:
        stack.append(trophy)
ans.append(len(stack))
trophyList.reverse()
stack=[]
for i ,trophy in enumerate(trophyList):
    if i==0:
        stack.append(trophy)
        continue
    if stack[-1]<trophy:
        stack.append(trophy)
ans.append(len(stack))
for i in ans:
    print(i)
        