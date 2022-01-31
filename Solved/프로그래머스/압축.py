def solution(msg):
    answer = []
    index_list=['0','A','B','C','D','E','F','G','H','I','J','K','L',
                'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    idx=0
    while idx<len(msg):
        temp=msg[idx]
        temp_index=index_list.index(temp)
        while temp in index_list :
            temp_index=index_list.index(temp)
            idx+=1
            if idx>=len(msg):
                break
            temp+=msg[idx]
        index_list.append(temp)
        answer.append(temp_index)
    return answer