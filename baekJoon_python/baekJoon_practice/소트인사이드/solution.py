target = input()
numList = list(map(int,target))
numList.sort(reverse=True)
print("".join(map(str,numList)))

    
