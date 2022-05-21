def solution(land):
    answer = 0
   
    for i in range(len(land)-1):
        temp_list= land[i+1].copy()
        for j in range(len(land[0])):
            for k in range(len(land[0])):
                if k==j: continue
                land[i+1][k]=max(land[i+1][k],temp_list[k]+land[i][j])
    answer=max(land[-1])
    return answer