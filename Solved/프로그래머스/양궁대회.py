isPossible = False
ans_list=[]
max_point=-1

def dfs(arrow_cnt,info,cur_point,cur_list,point,apeach_point):
    global isPossible, ans_list,max_point
    if point==0 :
        if arrow_cnt>0:
            cur_list[point]=arrow_cnt
            arrow_cnt=0
        if cur_point>apeach_point:
            isPossible=True
            temp_diff = cur_point-apeach_point
            if temp_diff>=max_point:
                if temp_diff==max_point:
                    if not isbest(cur_list):
                        return
                
                ans_list=cur_list.copy()
                max_point=temp_diff
        return
    
    if arrow_cnt>info[point]:
        temp_list=cur_list.copy()
        temp_list[point]=info[point]+1        
        dfs(arrow_cnt-info[point]-1,info,cur_point+point,temp_list,point-1,apeach_point)
    if info[point]>0:
        apeach_point+=point
    temp_list=cur_list.copy()
    dfs(arrow_cnt,info,cur_point,temp_list,point-1,apeach_point)
                
                
def isbest(cur_list):
    for i in range(11):
        if ans_list[i]<cur_list[i]:
            return True
        elif ans_list[i]>cur_list[i]:
            return False
    return True        
def solution(n, info):
    answer = [0]*11
    global max_point, apeach_point, ans_list
    
    info.reverse()
    dfs(n,info,0,answer,10,0)
    ans_list.reverse()
    
    if not isPossible:
        ans_list=[-1]
    
    return ans_list