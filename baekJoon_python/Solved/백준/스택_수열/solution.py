stackCnt=int(input())
list=[]
stack=[]
idx=1
check=True
for i in range(stackCnt) :
    temp = int(input())
    while idx<=temp :
        stack.append(idx)
        list.append("+")
        idx+=1
    comp=stack.pop()
    if comp!=temp:
        check=False
        break
    list.append("-")
if check:
    for str in list:
        print(str)
else :
    print("NO")