def solution(n):
    answer = 0
    cnt = bin(n).count('1')
    while True:
        n=n+1
        if bin(n).count('1')==cnt:
            answer=n
            break
    return answer