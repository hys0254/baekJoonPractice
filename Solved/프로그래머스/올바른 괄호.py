def solution(s):
    answer = True
    temp_stack=[]
    for str in s:
        if str=='(':
            temp_stack.append(str)
        elif str==')':
            if not temp_stack:
                answer=False
            else:
                temp_stack.pop()
    else:
        if temp_stack:
            answer=False
        

    return answer