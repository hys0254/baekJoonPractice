import math
student_cnt, case_cnt = map(int,input().split())
grade_list=list(map(int,input().split()))
ans=[]
for _ in range(case_cnt):
    start,end=map(int,input().split())
    # ans.append(f'{round(sum(grade_list[start-1:end])/(end-start+1),2):0.2f}')
    ans.append( "{:.2f}".format(round(sum(grade_list[start-1:end])/(end-start+1),2)))
for i in ans:
    print(i)