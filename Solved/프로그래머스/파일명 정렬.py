def solution(files):
    answer = []
    answer_temp=[]
    for file in files:
        temp=[]
        check=True
        hn_div=0
        nt_div=0
        for i in range(len(file)):
            if ord(file[i])>=ord('0')and ord(file[i])<=ord('9') and check:
                
                hn_div=i
                temp.append(file[:hn_div])
                check=False
            if (ord(file[i])<ord('0') or ord(file[i])>ord('9')) and not check:
                
                nt_div=i
                temp.append(file[hn_div:nt_div])
                temp.append(file[nt_div:])
                break
        else :
            temp.append(file[hn_div:])
            
        for i in range(len(answer_temp)):
            if answer_temp[i][0].lower()<temp[0].lower():
                continue
            elif answer_temp[i][0].lower()>temp[0].lower():
                answer_temp.insert(i,temp)
                answer.insert(i,file)
                break
            elif answer_temp[i][0].lower()==temp[0].lower():
                if int(answer_temp[i][1])<=int(temp[1]):
                    continue
                else:
                    answer_temp.insert(i,temp)
                    answer.insert(i,file)
                    break
        else:
            answer_temp.append(temp)
            answer.append(file)
     
                    
    return answer