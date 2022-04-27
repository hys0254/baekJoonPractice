item_cnt,wt_limit= map(int, input().split())
memory=[[0]*(wt_limit+1)for _ in range(item_cnt+1)]

for i in range(1,item_cnt+1):
    w,v = map(int,input().split())
    for j in range(1,wt_limit+1):
        if j<w:
            memory[i][j]=memory[i-1][j]
        else:
            memory[i][j]= max(memory[i-1][j],memory[i-1][j-w]+v)

print(memory[item_cnt][wt_limit])