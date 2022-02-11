g_arr=[]
answer=[0,0]
def compression(x,y,length):
    global answer
    check=True
    start_value=g_arr[x][y]
    for i in range(length):
        for j in range(length):
            if g_arr[x+i][y+j]!=start_value:
                check=False
    if check:
        answer[start_value]+=1
        return
    compression(x,y,length//2)
    compression(x+length//2,y,length//2)
    compression(x,y+length//2,length//2)
    compression(x+length//2,y+length//2,length//2)
    
def solution(arr):
    global g_arr
    g_arr=arr
    compression(0,0,len(arr))
    return answer