target = input()
testCase = input()
found = False
cnt=0
while target.find(testCase)!=-1 :
    target=target[target.find(testCase)+len(testCase):]
    cnt+=1
    
print(cnt) 