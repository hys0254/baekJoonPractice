def solution(m, musicinfos):
    answer = '(None)'
    maximum_playtime=-1
    for musicinfo in musicinfos:
        temp=musicinfo.split(',')
        start_time=list(map(int,temp[0].split(':')))
        end_time=list(map(int,temp[1].split(':')))
        play_time=end_time[0]*60+end_time[1]-start_time[0]*60-start_time[1]
        music=[]
        played_music=[]
        idx=0
        while idx<len(temp[3]):
            note_temp=temp[3][idx]
            if idx<len(temp[3])-1 and temp[3][idx+1]=='#':
                note_temp+=temp[3][idx+1]
                idx+=1
            music.append(note_temp)
            idx+=1
        music=music*(play_time//len(music))+music[:play_time%len(music)]
        idx=0
        while idx<len(m):
            note_temp=m[idx]
            if idx<len(m)-1 and m[idx+1]=='#':
                note_temp+=m[idx+1]
                idx+=1
            played_music.append(note_temp)
            idx+=1
      
        
        
        
        
        for note in range(len(music)-len(played_music)+1):
            
            if music[note]==played_music[0]:
               
                if music[note:note+len(played_music)]==played_music and len(music)>maximum_playtime:
                    answer=temp[2]
                    maximum_playtime=len(music)
        else:
            if music==played_music and len(music)>maximum_playtime:
                answer=temp[2]
                maximum_playtime=len(music)
        
        
            
    return answer