def dfs (m,hm,bc,i,j):
    hm[i][j]=1
    m[i][j]=bc
    for idx in range(4):
        nx=dx[idx]+i
        ny=dy[idx]+j
        if nx<0 or ny<0 or nx>len(m)-1 or ny>len(m)-1 or hm[nx][ny]==1 or m[nx][ny]==0:
            continue
        dfs(m,hm,bc,nx,ny)

    
    

row_cnt= int(input())
map=[]
hit_map = [[0]*row_cnt for _ in range(row_cnt)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
for _ in range(row_cnt):
    temp=[]
    for str in list(input()):
        temp.append(int(str))
    
    map.append(temp)
block_cnt=1
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j]==0 or hit_map[i][j]==1:
            continue
        else :
            
            dfs(map,hit_map,block_cnt,i,j)
            
            block_cnt+=1
ans=[0]*(block_cnt-1)

for list in map:
    for i in range(1,block_cnt):
        ans[i-1]+=list.count(i)
print(block_cnt-1)
ans.sort()
if block_cnt-1==0:
    print(0)
else : 
    for i in ans:
        print(i)
            
