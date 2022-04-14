def search(X,Y,range):
    global ans,found
    if found==True:
        return
    if range==2:
        
        if X==r and Y==c:
            found=True
            print(ans)
            return          
        ans+=1
        if X==r and Y+1==c:
            found=True
            print(ans)
            return
        ans+=1
        if X+1==r and Y==c:
            found=True
            print(ans)
            return
        ans+=1
        if X+1==r and Y+1==c:
            found=True
            print(ans)
            return
        ans+=1
        return
    
    
    if found==True:
        return
    search(X,Y,range/2)
    if found==True:
        return
    search(X,Y+range/2,range/2)
    if found==True:
        return
    search(X+range/2,Y,range/2)
    if found==True:
        return
    search(X+range/2,Y+range/2,range/2)

ans=0
found = False
N,r,c = map(int,input().split(' '))
search(0,0,2**N)
    


    