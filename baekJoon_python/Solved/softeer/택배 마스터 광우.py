
def dfs(cur_raillist,hit_list):
    global ans_wt
    if False not in hit_list:
        idx=0
        temp_min=0
        for i in range(job_cnt):
            cur_boxwt=0
            while cur_boxwt+cur_raillist[idx%rail_cnt]<=max_wt:
                cur_boxwt+=cur_raillist[idx%rail_cnt]
                # if cur_boxwt+temp_min>=ans_wt:
                #     return
                idx+=1
            temp_min+=cur_boxwt
            # if temp_min>=ans_wt:
            #     return
        ans_wt=min(temp_min,ans_wt)
        return
    for i in range(rail_cnt):
        if hit_list[i]:
            continue
        tempcur_raillist=cur_raillist.copy()
        temphit_list=hit_list.copy()
        tempcur_raillist.append(rail_list[i])
        temphit_list[i]=True
        dfs(tempcur_raillist,temphit_list)
        
    
rail_cnt, max_wt, job_cnt = map(int,input().split())
rail_list = list(map(int,input().split()))
ans_wt=max_wt*job_cnt

        
for i in range(rail_cnt):
    cur_raillist=[rail_list[i]]
    hit_list=[False]*rail_cnt
    hit_list[i]=True
    dfs(cur_raillist,hit_list)

print(ans_wt)
