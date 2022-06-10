import heapq
def solution(scoville, K):
    answer = 0
    scoville.sort()
    heapq.heapify(scoville)
    for _ in range(len(scoville)-1):
        min1=heapq.heappop(scoville)
        min2=heapq.heappop(scoville)
        new_food = heapq.heappush(scoville,min1+min2*2)
        answer+=1
        if scoville[0]>=K:
            break
    if scoville[0]<K:
        return -1
        
    return answer

