def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp_list=[0]*len(arr2[0])
        for j in range(len(arr1[0])):
            for k in range(len(arr2[0])):
                temp_list[k]+=arr1[i][j]*arr2[j][k]
        answer.append(temp_list)    
            
    return answer