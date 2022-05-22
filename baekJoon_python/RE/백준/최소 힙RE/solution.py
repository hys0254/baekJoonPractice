import sys
import heapq
n= int(sys.stdin.readline())
heap=[]
result=[]
for _ in range(n):
    input_num = int(sys.stdin.readline())
    if input_num ==0:
        if heap:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
    else:
        heapq.heappush(heap,input_num)
        
for num in result:
    print(num)