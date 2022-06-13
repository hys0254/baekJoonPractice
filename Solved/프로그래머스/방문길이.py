def solution(dirs):
    dir=[[-1,0],[1,0],[0,-1],[0,1]]
    answer = 0
    visit_list={}
    current_pos=(0,0)

    for move in dirs:
        next_pos=[]
        if move =="U":
            next_pos=(current_pos[0]+dir[0][0],current_pos[1]+dir[0][1])
            if (next_pos[0]<-5 or next_pos[0]>5 or
                next_pos[1]<-5 or next_pos[1]>5):
                
                continue    
        elif move=="D":
            next_pos=(current_pos[0]+dir[1][0],current_pos[1]+dir[1][1])
            if (next_pos[0]<-5 or next_pos[0]>5 or
                next_pos[1]<-5 or next_pos[1]>5):
                
                continue
        elif move =="L":
            next_pos=(current_pos[0]+dir[2][0],current_pos[1]+dir[2][1])
            if (next_pos[0]<-5 or next_pos[0]>5 or
                next_pos[1]<-5 or next_pos[1]>5):
                
                continue            
        elif move=="R":
            next_pos=(current_pos[0]+dir[3][0],current_pos[1]+dir[3][1])
            if (next_pos[0]<-5 or next_pos[0]>5 or
                next_pos[1]<-5 or next_pos[1]>5):
                
                continue            
        if (next_pos not in visit_list.get(current_pos,set())
            or current_pos not in visit_list.get(next_pos,set())):
                
                answer+=1
        temp1=visit_list.get(current_pos,set())
        temp1.add(next_pos)
        visit_list[current_pos]=temp1
        temp2=visit_list.get(next_pos,set())
        temp2.add(current_pos)
        visit_list[next_pos]=temp2
        current_pos=next_pos
        
    
    return answer