def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        idx=0
        stack=[]
        for ch in skill_tree:
            if ch in skill:
                if ch==skill[idx]:
                    idx+=1
                else:
                    break
        else:
            answer+=1
        
    return answer