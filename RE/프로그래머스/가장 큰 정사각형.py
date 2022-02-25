
def solution(board):
    answer=0
    for row in board:
        answer=max(answer,max(row))

    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j]==1:
                board[i][j]=min(min(board[i][j-1],board[i-1][j]),board[i-1][j-1])+1
                answer=max(board[i][j],answer)

    return answer**2
