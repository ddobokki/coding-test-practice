import math
def solution(gems):
    total_gem = len(set(gems))
    gem_dic ={}

    temp = []
    cur_dist = math.inf
    is_change_start = False
    start = 0
    for i,g in enumerate(gems):
        if g in gem_dic:
            if gem_dic[g] == start:
                is_change_start = True

        gem_dic[g] = i
        if len(gem_dic) == total_gem:
            if is_change_start:
                start = min(gem_dic.values())
                is_change_start = False

            end = i

            if cur_dist > (end - start):
                temp = [start + 1, end + 1]
                cur_dist = (end - start)

                # if cur_dist + 1 == total_gem:
                #     break

    return temp

solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
#solution(["AA", "AB", "AC", "AA", "AC"])
#solution(["XYZ", "XYZ", "XYZ"])
#solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])