import copy
def dfs(start_pos,pre_hitmap,pre_direction,preAns_list,moving_distance):
    global min_command,min_commandlength
    if moving_distance>=road_cnt :
        
        
        if min_commandlength>len(preAns_list):
            min_commandlength=len(preAns_list)
            min_command="".join(preAns_list)
        return
            
    
    
    for i in range(4):
        tempAns_list=preAns_list.copy()
        temp_hitmap=copy.deepcopy(pre_hitmap)
        nx=start_pos[0]+dx[i]
        ny=start_pos[1]+dy[i]
        if (nx+start_pos[0])/2<0 or (ny+start_pos[1])/2<0 or (nx+start_pos[0])/2>H-1 or (ny+start_pos[1])/2>W-1:
            continue
        if nx<0 or ny<0 or nx>H-1 or ny>W-1 :
            continue
        if temp_hitmap[nx][ny]==1 or temp_hitmap[int((start_pos[0]+nx)/2)][int((start_pos[1]+ny)/2)]==1:
            continue
        if map[nx][ny]=='.' or map[int((start_pos[0]+nx)/2)][int((start_pos[1]+ny)/2)]=='.':
            continue
        if i != pre_direction:
            tempAns_list.append(change_direction[(pre_direction,i)])

        tempAns_list.append('A')
        temp_hitmap[nx][ny]=1
        temp_hitmap[int((start_pos[0]+nx)/2)][int((start_pos[1]+ny)/2)]=1
        dfs([nx,ny],temp_hitmap,i,tempAns_list,moving_distance+2)
        
#입력

dx=[0,0,2,-2]
dy=[-2,2,0,0]
direction=['<','>','v','^']
change_direction={
    (0,1):'LL',
    (0,2):'L',
    (0,3):'R',
    (1,0):'RR',
    (1,2):'R',
    (1,3):'L',
    (2,0):'R',
    (2,1):'L',
    (2,3):'LL',
    (3,0):'L',
    (3,1):'R',
    (3,2):'RR', 
}
H, W = map(int, input().split())
hit_map=[[0]*W for _ in range(H)]
map=[]
min_command=''
min_commandlength=10*H*W
road_cnt=0
for _ in range(H):
    map.append(list(input()))
startPos_list=[]
#시작점 찾기
for x in range(H):
    for y in range(W):
        if map[x][y]=='#':
            startPos_list.append((x,y))
            road_cnt+=1

for start_pos in startPos_list:
        for k in range(4):
          
            start_hitmap=copy.deepcopy(hit_map)
            start_hitmap[start_pos[0]][start_pos[1]] =1
            tempAns_list=[str(start_pos[0]),str(start_pos[1]),direction[k]]
            dfs(start_pos,start_hitmap,k,tempAns_list,1)

print(int(min_command[0])+1,int(min_command[1])+1)
print(min_command[2])
print(min_command[3:])
            
         
        