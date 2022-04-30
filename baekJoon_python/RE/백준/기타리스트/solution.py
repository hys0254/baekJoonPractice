from collections import deque

def solution(queue1, queue2):
   
    sum_q=0
    answer = -2
    q1 = deque(list(map(int,queue1)))
    q2 = deque(list(map(int,queue2)))
    
    sum_q = sum(queue1)+sum(queue2)
    cnt=0
    while q1 and q2:
        if sum(q2)<sum_q/2:
            q2.append(q1.popleft())
        elif sum(q1)<sum_q/2:
            q1.append(q2.popleft())
        cnt+=1
        if sum(q2)==sum_q/2 and sum(q1)==sum_q/2:
            break
        if list(q1)==queue1 and list(q2)==queue2:
            cnt=(-1)
            break
    print(cnt)


    return answer
