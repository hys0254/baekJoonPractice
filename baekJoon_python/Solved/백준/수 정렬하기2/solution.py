import sys
caseCnt = int(input())
numArr=[]
for _ in range(caseCnt):
    numArr.append(int(sys.stdin.readline()))
numArr.sort()
for i in numArr:
    print(i)