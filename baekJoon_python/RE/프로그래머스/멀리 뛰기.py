def solution(n):
    answer = []
    for i in range(n):
        if i<2:
            answer.append(i+1)
        else :
            answer.append(answer[i-1]%1234567+answer[i-2]%1234567)
        
    
    return answer[-1]