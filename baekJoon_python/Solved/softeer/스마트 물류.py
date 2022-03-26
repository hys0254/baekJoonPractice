line_length, arm_length = map(int,input().split())

line = input()
line=line.replace('H','0')
line=line.replace('P','1')
line=list(map(int,line))

for i in range(line_length):
    if line[i]!=1:
        continue
    for j in range(i-arm_length,i+arm_length+1):
        if j>line_length-1 or j<0:
            continue
        if line[j]==0:
            line[j]=-1
            break
print(line.count(-1))