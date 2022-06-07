ans_list=set()
sn_list=set()
idx=1
while idx<=10000:
    
    if idx not in sn_list:
        ans_list.add(idx)
    else :
        idx+=1
        continue
    temp=list(str(idx))
    sn=idx
    for i in temp:
        sn+=int(i)
    sn_list.add(sn)
    while sn<=10000:
        temp=list(str(sn))
        for i in temp:
            sn+=int(i)
        sn_list.add(sn)
    idx+=1
ans_list=list(ans_list)
ans_list.sort()
for ans in ans_list:
    print (ans)
    
