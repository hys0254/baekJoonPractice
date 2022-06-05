max_queen=0
answer=0
chessboard=[]
def columnCheck(x,y):
    while x>0:
        x-=1
        if chessboard[x][y]==1:
            return False
    return True
    
def diagonalCheck(x,y):
    global chessboard
    temp_x=x
    temp_y=y
    while x>0 and y>0:
        x-=1
        y-=1
        if chessboard[x][y]==1:
            return False
    x=temp_x
    y=temp_y
    while x>0 and y<max_queen-1:
        x-=1
        y+=1
        if chessboard[x][y]==1:
            return False
    return True
    
def dfs(remain_Queen):
    global answer
    global chessboard
    if remain_Queen==0:
        
        answer+=1
        return
    for i in range(len(chessboard[0])):
        if columnCheck(max_queen-remain_Queen,i) and diagonalCheck(max_queen-remain_Queen,i):
            chessboard[max_queen-remain_Queen][i]=1
            dfs(remain_Queen-1)
            chessboard[max_queen-remain_Queen][i]=0
    return
            
        
def solution(n):
    global max_queen
    global answer
    global chessboard
    max_queen=n
    chessboard=[[0 for _ in range(n)] for _ in range (n)]
    dfs(n)
    return answer
