stone_cnt = int(input())
stone_list = list(map(int,input().split()))

listA=[]
listB=[1]*stone_cnt

for i in range(stone_cnt):
    if not listA:
        listA.append(stone_list[i])
        continue
    start=0
    target=0
    end=len(listB)-1
    while start<=end:
        mid=(start+end)//2
        target=mid
        if listA[mid]<stone_list[i]:
            end=mid-1
        else:
            start=mid+1
    if mid<stone_
    
    