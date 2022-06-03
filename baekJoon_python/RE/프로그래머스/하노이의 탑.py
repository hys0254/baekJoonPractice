def solution(n):
    answer = []
    def hanoi(n,From,To,Sub):
        if n==1:
            answer.append([From,To])
            return
        hanoi(n-1,From,Sub,To)
        answer.append(From,To)
        hanoi(n-1,Sub,To,From)
    hanoi(n,1,3,2)
    return answer