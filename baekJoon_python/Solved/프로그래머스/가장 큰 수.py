from itertools import permutations


def solution(numbers):
    answer = ''
    temp_list=[]
    
    for i in numbers:
        temp_list.append(str(i))
    
    per=permutations(temp_list,len(temp_list))
    for i in per:
        print(i)
    
    
    return 