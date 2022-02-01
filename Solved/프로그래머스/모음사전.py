# def solution(word):
#     answer = 0
#     dict=['A','E','I','O','U']
#     for i in range(len(word)):
#         if word[i]==dict[0]:
#             answer+=1
#         else:
#             temp=dict.index(word[i])
#             for j in range(5-i):
#                 answer+=temp*(5**j)
#             answer+=1
        
    
#     return answer+1\
    
    
    
def solution(word):
    answer = 0
    dict=['A','E','I','O','U']
    for i in range(len(word)):
       
        temp=dict.index(word[i])
        for j in range(5-i):
            answer+=temp*(5**j)
        answer+=1
        
    
    return answer