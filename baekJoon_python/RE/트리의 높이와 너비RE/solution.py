node_cnt = int(input())
tree=[]
root, left, right = map(int, input().split())
tree.append({root,1})
print(tree.index(root))
# for _ in range(node_cnt):
#     root, left, right = map(int, input().split())
#     tree.append