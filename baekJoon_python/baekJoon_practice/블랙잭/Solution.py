temp= list(map(int,input().split(' ')))
cardCnt =temp[0]
max=temp[1]
cardList=list(map(int,input().split(' ')))
cardSum=0
for i in range(0,cardCnt):
    for j in range(i+1,cardCnt):
        for k in range(j+1,cardCnt):
            print("i : ",i," j : ",j," k : ",k)
            if cardList[i]+cardList[j]+cardList[k]>max:
                continue
            if cardSum<cardList[i]+cardList[j]+cardList[k]:
                cardSum=cardList[i]+cardList[j]+cardList[k]
                
print(cardSum)
