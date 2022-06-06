import sys
case_num = int (sys.stdin.readline())
ans_list=[]

for _ in range(case_num):
    test_case= sys.stdin.readline().split()
    for i in range(len(test_case)):
        test_case[i]=test_case[i][::-1]
    ans_list.append(test_case)
    
for str_list in ans_list:
    for str in str_list:
        if str == str_list[-1]:
            print(str)
        else:
            print(str,end=' ')
