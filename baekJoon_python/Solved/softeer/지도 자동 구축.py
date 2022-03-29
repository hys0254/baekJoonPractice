cnt=int(input())
list=[2]
for i in range(cnt):
    list.append(list[-1]+list[-1]-1)
print(list[-1]**2)