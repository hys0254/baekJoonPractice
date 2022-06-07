N,M = map(int, input().split())
cnt=0
row =[0]*M
column =[0]*N

for j in range(N):
    line =input()
    flag =True
    for i in range(M):
        print(line[i])
        if row[i]==1:
            continue
        if line[i]=="X":
            row[i]=1
            
    if "X" in line:
        column[j]=1
    
print(column)
print(row)
print(max(column.count(0),row.count(0)))
            