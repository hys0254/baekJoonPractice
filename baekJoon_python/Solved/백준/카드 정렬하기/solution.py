import heapq
heap=[]
case_cnt= int(input())
for _ in range(case_cnt):
    heapq.heappush(heap,int(input()))
ans=0

while len(heap) !=1:
    curA=heapq.heappop(heap)
    curB=heapq.heappop(heap)
    ans+=curA+curB
    heapq.heappush(heap,curA+curB)
print(ans)