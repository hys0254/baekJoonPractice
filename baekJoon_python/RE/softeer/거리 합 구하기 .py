def dfs1(current,parent):
    for child in connect_list[current].keys():
        if child == parent:
            continue
        dfs1(child,current)
        ans_list[current]+=connect_list[current][child]*subtree_list[child]+ans_list[child]
        subtree_list[current]+=subtree_list[child]

def dfs2(current,parent):
    for child in connect_list[current].keys():
        if child==parent:
            continue
        print(ans_list[current]+(n-subtree_list[child])*connect_list[current][child]-(subtree_list[child])*connect_list[current][child])
        ans_list[child]=ans_list[current]+(n-subtree_list[child])*connect_list[current][child]-(subtree_list[child])*connect_list[current][child]
        dfs2(child,current)
   

n=int(input())
connect_list=[dict() for _ in range(n+1)]
subtree_list=[1 for _ in range(n+1)]
ans_list=[0 for _ in range(n+1)]
for _ in range(n-1):
    start_node, end_node, length = map(int,input().split())
    connect_list[start_node][end_node]=length
    connect_list[end_node][start_node]=length

dfs1(1,1)
dfs2(1,1)

print(subtree_list)
print(ans_list)