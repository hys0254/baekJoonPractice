class Node:
    def __init__(self,data,left,right):
        self.parent=-1
        self.data=data
        self.left_node=left
        self.right_node=right
        
def in_order(node,level):
    global level_depth,x
    level_depth=max(level_depth,level)
    if tree[node].left_node != -1:
        in_order(tree[node].left_node,level+1)
    min_level[level]=min(min_level.get(level,node_cnt),x)
    max_level[level]=max(max_level.get(level,0),x)
    x+=1
    if tree[node].right_node != -1:
        in_order(tree[node].right_node,level+1)

x=1
min_level={}
max_level={}
node_cnt=int(input())
level_depth=1
root=0
tree={}

for i in range(1,node_cnt+1):
    tree[i]= Node(i,-1,-1)
    
for _ in range(node_cnt):
    root,left,right=map(int,input().split())
    tree[root].left_node=left
    tree[root].right_node=right
    if left != -1:
        tree[left].parent=root
    if right != -1:
        tree[right].parent=root

for i in range(1,node_cnt+1):
    if tree[i].parent== -1:
        root=i
        break
    
in_order(root,1)
result_level=1
result_width=max_level[1]-min_level[1]+1

for i in range(2,level_depth+1):
    if result_width<max_level[i]-min_level[i]+1:
        result_level=i
        result_width=max_level[i]-min_level[i]+1
        
print(result_level,result_width)