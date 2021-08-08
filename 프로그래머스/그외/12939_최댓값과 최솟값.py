def solution(s):
    s = s.split()
    s_list = list(map(lambda x:int(x),s))

    return str(min(s_list))+" "+str(max(s_list))

print(solution("1 2 3 4"))