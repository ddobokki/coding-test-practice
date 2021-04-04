def check(li, num_of_gems):
    if len(set(li)) == num_of_gems:
        return True
    else:
        return False


def solution(gems):
    num_of_gems = len(set(gems))
    if len(gems) == num_of_gems:
        return [1, num_of_gems]

    min_i = num_of_gems
    answer = min_i
    while True:
        #print(min_i)
        for i in range(len(gems) - min_i + 1):
            #print(i, i + min_i)
            if check(gems[i:i + min_i], num_of_gems):
                return [i+1, i + min_i]
        min_i += 1

    # for i in range(len(gems) - answer):
    #     print(check(gems[i:i + answer], num_of_gems))
    #     print(gems[i:i + answer])
    #     if check(gems[i:i + answer], num_of_gems):
    #         return [i + 1, i + 1 + answer]


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
# print(any([False,False,True]))
