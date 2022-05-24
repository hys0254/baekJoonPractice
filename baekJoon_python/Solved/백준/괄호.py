import sys
case_num = int(sys.stdin.readline())
ans_list=[]
for _ in range(case_num):
    case=list(sys.stdin.readline())
    stack=[]
    for ps in case:
        
        if ps =="(":
            stack.append(ps)
        elif ps==")" :
            if stack:
                stack.pop()
            else:
                stack.append(ps)
                break
    if stack:
        ans_list.append("NO")
    else:
        ans_list.append("YES")
        
        
for ans in ans_list:
    print(ans)