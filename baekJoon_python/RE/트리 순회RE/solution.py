class Node :
    def __init__(self,data,left_node,right_node):
        self.data=data
        self.left_node=left_node
        self.right_node=right_node
        
        
def pre_order(node):
    print(tree[node].data,end='')
    if tree[node].left_node != '.':
        pre_order(tree[node].left_node)
    if tree[node].right_node != '.':
        pre_order(tree[node].right_node)
        
def in_order(node):
    if tree[node].left_node != '.':
        in_order(tree[node].left_node)
    print(tree[node].data,end='')
    if tree[node].right_node != '.':
        in_order(tree[node].right_node)
        
def post_order(node):
    if tree[node].left_node != '.':
        post_order(tree[node].left_node)
    if tree[node].right_node != '.':
        post_order(tree[node].right_node)
    print(tree[node].data,end='')

node_cnt = int(input())
tree={}
for _ in range(node_cnt):
    root, left, right = input().split()
    tree[root]=Node(root,left,right)
    
pre_order('A')
print()
in_order('A')
print()
post_order('A')