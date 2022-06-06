from math import factorial
def solution(n, k):
    answer = []
    people = [i for i in range(1,n+1)]
    while n != 0:
        count = factorial(n)//n
        target = k//count
        k=k%count
        if k==0:
            answer.append(people.pop(target-1))
        else :
            answer.append(people.pop(target))
        n-=1
    return answer