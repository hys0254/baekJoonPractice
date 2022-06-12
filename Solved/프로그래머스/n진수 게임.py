def conv(idx,n):
    if idx==0:
        return '0'
    temp=''
    while idx!=0:
        quot=idx//n
        remain=idx%n
        if remain>9:
            temp=chr(remain-10+65)+temp
        else :
            temp=str(remain)+temp
        idx=quot
    
    return temp

def solution(n, t, m, p):
    answer = ''
    idx=0
    temp=''
    while len(answer) != t:
        print(idx)
        temp+=conv(idx,n)
        print(temp)
        while len(temp)>=m:
            
            
            answer+=temp[p-1]
            temp=temp[m:]
        idx+=1
            
 
    return answer


print(solution(16,16,2,2))