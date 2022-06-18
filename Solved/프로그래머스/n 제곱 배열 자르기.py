def solution(n, left, right):
    answer = []
    for i in range(left,right):
        sub, remain = i//n,i%n
        if remain<=sub:
            answer.append(sub+1)
        elif remain>sub:
            answer.append(sub+1+remain-sub)
    return answer