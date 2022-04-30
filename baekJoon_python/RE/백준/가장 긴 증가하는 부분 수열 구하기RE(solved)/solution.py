numArr_length= int(input())
numArr=list(map(int,input().split()))
memory=[1]*numArr_length

for i in range(1,numArr_length):
    for j in range(0,i):
        if numArr[j]<numArr[i]:
            memory[i]=max(memory[i],memory[j]+1)

print(max(memory))
        