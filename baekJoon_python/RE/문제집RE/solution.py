import heapq
q_cnt, info_cnt= map(int, input().split())
heap=[]
for _ in range(info_cnt):
    a,b = map(int,input().split())
    heapq.heappush(heap,(a,b))
ans_list=[]
pass_list=[]
print(heap)
for i in range(1,q_cnt+1):
    if i in pass_list:
        continue
    if heap:
        x=heapq.heappop(heap)
        if x[1]==i:
            ans_list.append(x[0])
            pass_list.append(x[0])
        else:
            heapq.heappush(heap,x)
            
   
    ans_list.append(i)
    pass_list.append(i)
    
for i in ans_list:
    print(i,end=' ')