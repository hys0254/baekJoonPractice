from collections import deque
island_cnt, bridge_cnt = map(int, input().split())
bridgeInfo=[[] for _ in range(island_cnt+1)]
def bfs(mid):
    visitList=[False for _ in range(island_cnt+1)]
    
    queue=deque([start_node])
    visitList[start_node]=True
    while queue:
        cur_pos = queue.popleft()
        for to, wt in bridgeInfo[cur_pos]:
            if not visitList[to] and wt>=mid:
                visitList[to]=True
                queue.append(to)
    
    return visitList[end_node]

wt_min, wt_max = 1000000001,0
for _ in range(bridge_cnt):
    start, end, wt_limit = map(int, input().split())
    bridgeInfo[start].append((end,wt_limit))
    bridgeInfo[end].append((start,wt_limit))
    wt_min= min(wt_min,wt_limit)
    wt_max=max(wt_max,wt_limit)

start_node, end_node = map(int, input().split())
result= wt_min
while wt_min<=wt_max:
    mid = (wt_min+wt_max)//2
    
    if bfs(mid):
        result=mid
        wt_min=mid+1
    else:
        wt_max=mid-1      
print(result)