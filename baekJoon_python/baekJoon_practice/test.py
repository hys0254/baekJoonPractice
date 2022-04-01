import queue

data=[[0]*i for i in range(2)]
for i in range(2):
    for j in range(10):
        data[i].append(i*10+j)
temp = queue.PriorityQueue()
temp.put((3,"hi"))
temp.put((4,"hello"))
       
for i in range(2):
    for j in range(10):
        print(data[i][j],end=" ")
    print()
    
print(temp.get()[0])
