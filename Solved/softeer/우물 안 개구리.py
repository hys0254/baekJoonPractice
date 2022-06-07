
n,m = map(int,input().split())
wt_list= [0]+list(map(int,input().split()))
friendship_dict=[set() for _ in range(n+1)]

for _ in range(m):
    memA,memB=map(int,input().split())
    friendship_dict[memA].add(memB)
    friendship_dict[memB].add(memA)

frog_cnt=0

for key in range(1,n+1):
    wt=wt_list[key]
    frog_cnt+=1
    for friend_key in friendship_dict[key]:
        if wt<=wt_list[friend_key]:
            frog_cnt-=1
            break

print(frog_cnt)