# 암호표 제작
def create_cyphergraph(ck,cg):
    temp=[]
    for str in list(ck):
        if str not in temp:
            temp.append(str)
    for str in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        if str =='J':
            continue
        if str not in temp:
            temp.append(str)
    for i in range(5):
        cg.append(temp[i*5+0:i*5+5])
        
def encrypting1(mg):
    temp=[]
    i=0
    while i< len(mg):
        
        if i==len(mg)-1:
            temp.append([mg[i],'X'])
            i+=1
            continue
        if mg[i]!=mg[i+1]:
            temp.append([mg[i],mg[i+1]])
            i+=2
            continue
        else:
            if mg[i]!='X':
                temp.append([mg[i],'X'])
            else:
                temp.append([mg[i],'Q'])
            i+=1
    
    return temp

def encrypting2(cg,cy):
    for str_list in cy:
        first_pos=[]
        second_pos=[]
        for i in range(len(cg)):
            if str_list[0] in cg[i]:
                first_pos=[i,cg[i].index(str_list[0])]
            if str_list[1] in cg[i]:
                second_pos=[i,cg[i].index(str_list[1])]
        if first_pos[0]==second_pos[0] or (first_pos[0]==second_pos[0] and first_pos[1]==second_pos[1]) :
            str_list[0]=cg[first_pos[0]][(first_pos[1]+1)%5]
            str_list[1]=cg[second_pos[0]][(second_pos[1]+1)%5]
        elif first_pos[1]==second_pos[1]:
            str_list[0]=cg[(first_pos[0]+1)%5][first_pos[1]]
            str_list[1]=cg[(second_pos[0]+1)%5][first_pos[1]]
        else:
            str_list[0]=cg[first_pos[0]][second_pos[1]]
            str_list[1]=cg[second_pos[0]][first_pos[1]]
            
            


cypher_graph=[]
message=input()
cypher_key = input()
create_cyphergraph(cypher_key,cypher_graph)
cypher=encrypting1(message)

encrypting2(cypher_graph,cypher)

for str_list in cypher:
    print(str_list[0],end='')
    print(str_list[1],end='')
