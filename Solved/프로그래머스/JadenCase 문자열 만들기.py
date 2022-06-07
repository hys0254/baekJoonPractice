def solution(s):
    answer = ''
    s=s.lower()
    idx=0
    while idx<len(s):
        if s[idx] ==' ':
            answer+=s[idx]
            idx+=1
            continue
        if (idx-1>=0 and s[idx-1]==' ' and s[idx].islower()) or(idx==0 and s[idx].islower()):
            answer+=s[idx].upper()
        else:
            answer+=s[idx]
        idx+=1
            
        
    return answer