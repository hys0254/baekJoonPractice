birdCnt = int(input())
idx =1
ans=0
while birdCnt>0 :
    if birdCnt>=idx:
        birdCnt-=idx
        ans+=1
        idx+=1
    else :
        idx=1
print(ans)