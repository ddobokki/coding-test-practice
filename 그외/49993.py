#https://programmers.co.kr/learn/courses/30/lessons/49993

#"CBD"	["BACDE", "CBADF", "AECB", "BDA"]	2

def solution(skill, skill_trees):
    skill_indexs = []
    for s in skill_trees:
        temp = [""] * len(s)
        for i in range(len(skill)):
            skill_index = s.find(skill[i])
            if (skill_index != -1):
                temp[skill_index] = skill[i]
        skill_indexs.append("".join(temp))

    fail = []
    for i in range(len(skill)):
        temp_s = skill[0:i + 1]
        for j in range(len(skill_indexs)):
            # print(skill_indexs[j][0:i+1], "-", temp_s)
            if not skill_indexs[j][0:i + 1] in temp_s:
                # print(j)
                fail.append(j)
    fail = set(fail)
    return len(skill_trees) - len(fail)

'''
def solution(skill,skill_tree):
    answer=0
    for i in skill_tree:
        skillist=''
        for z in i:
            if z in skill:
                skillist+=z
        if skillist==skill[0:len(skillist)]:
            answer+=1
    return answer
    
모범코드
짧다....
너무 복잡하게 생각한듯

'''



print(solution("CBD",	["BACDE", "CBADF", "AECB", "BDA"]))

print("" in "ABC")