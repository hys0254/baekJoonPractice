light_list=[[1,1,1,0,1,1,1],
            [0,0,1,0,0,1,0],
            [1,0,1,1,1,0,1],
            [1,0,1,1,0,1,1],
            [0,1,1,1,0,1,0],
            [1,1,0,1,0,1,1],
            [1,1,0,1,1,1,1],
            [1,1,1,0,0,1,0],
            [1,1,1,1,1,1,1],
            [1,1,1,1,0,1,1],
            [0,0,0,0,0,0,0]]
testcase_cnt=int(input())
ans_list=[]
for _ in range(testcase_cnt):
    switch_cnt=0
    blank=[10,10,10,10,10]
    before,after=input().split()
    before=list(map(int,before))
    after=list(map(int,after))
    before.reverse()
    after.reverse()
    before=before+blank[len(before):]
    after=after+blank[len(after):]
    for i in range(5):
        for j in range(7):
            if light_list[before[i]][j]!=light_list[after[i]][j]:
                switch_cnt+=1
    ans_list.append(switch_cnt)
for i in ans_list:
    print(i)
    