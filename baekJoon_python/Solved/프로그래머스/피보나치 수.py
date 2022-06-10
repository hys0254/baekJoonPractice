fib_list=[0,1]
def solution(n):
    while not len(fib_list)==n+1:
        fib_list.append(fib_list[-1]+fib_list[-2])
    return fib_list[n]%1234567