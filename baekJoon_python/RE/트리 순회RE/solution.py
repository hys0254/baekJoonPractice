class Node:
    def __init__(self,left_node,right_node,data):
        self.data=data
        self.left_node=left_node
        self.right_node=right_node
        
def pre_order(node):
    print(node.data,end='')
    if node.left_node !='.' :
        pre_order(tree[node.left_node])
    if node.right_node !='.' :
        pre_order(tree[node.right_node])
        
def in_order(node):
    
    if node.left_node !='.' :
        in_order(tree[node.left_node])
    print(node.data,end='')
    if node.right_node !='.' :
        in_order(tree[node.right_node])
        
def post_order(node):
    
    if node.left_node !='.' :
        post_order(tree[node.left_node])
    if node.right_node !='.' :
        post_order(tree[node.right_node])
        
    print(node.data,end='')
    
node_cnt= int(input())
tree={}
for _ in range(node_cnt):
    root, left, right = input().split()
    tree[root]=Node(left,right,root)
    
pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
    