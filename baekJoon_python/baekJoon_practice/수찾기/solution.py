n =int(input())
nlist=list(map(int,input().split(" ")))
ndict=dict()
for i in range(n):
    ndict[nlist[i]]=1
m=int(input())
mlist=list(map(int,input().split(" ")))

for i in range(m):
    print(ndict.get(mlist[i],0))
    