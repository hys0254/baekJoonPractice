melody =list(input().split())
ans=""
print(melody[8])
if int(melody[0])==1 :
    ans="ascending"
    for i in range(7):
        if melody[i]>melody[i+1]:
            ans="mixed"
elif int(melody[0])==8 :
    ans="descending"
    for i in range(7):
        if melody[i]<melody[i+1]:
            ans="mixed"
else :
    ans="mixed"
print(ans)


    