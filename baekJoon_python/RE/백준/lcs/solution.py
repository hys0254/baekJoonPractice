list_A = list(input())
list_B = list(input())
memory =[[0 for _ in range(len(list_A)+1)]for _ in range(len(list_B)+1)]
for i in range(1,len(list_B)+1):
    for j in range(1,len(list_A)+1):
        if list_B[i-1]==list_A[j-1]:
            memory[i][j]=memory[i-1][j-1]+1
        else :
            memory[i][j]=max(memory[i-1][j],memory[i][j-1])

print (memory[-1][-1])