
cnt=int(input())
zo_list=[0,1,2]
for i in range(3,cnt+1):
    zo_list.append((zo_list[i-2]+zo_list[i-1])%15746)
print(zo_list[-1])