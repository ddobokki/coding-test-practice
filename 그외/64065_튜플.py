# https://programmers.co.kr/learn/courses/30/lessons/64065

'''
s	result
"{{2},{2,1},{2,1,3},{2,1,3,4}}"	[2, 1, 3, 4]
"{{1,2,3},{2,1},{1,2,4,3},{2}}"	[2, 1, 3, 4]
"{{20,111},{111}}"	[111, 20]
"{{123}}"	[123]
"{{4,2,3},{3},{2,3,4,1},{2,3}}"	[3, 2, 4, 1]


'''


def solution(s):
    # 문자열 {} > 리스트로?
    s_list = s.split("},")
    s_list = list(map(lambda x: x.replace("{", "").replace("}", ""), s_list))
    # {}로 묶인 값을을 문자열로 가지는 리스트로 전환 {{2},{2,1},{2,1,3},{2,1,3,4}} -> ['2', '2,1', '2,1,3', '2,1,3,4']
    s_list = list(map(lambda x: x.split(','), s_list))
    # 각 값을 리스트로 전환 ['2', '2,1', '2,1,3', '2,1,3,4'] -> [['2'], ['2', '1'], ['2', '1', '3'], ['2', '1', '3', '4']]
    s_list = list(map(lambda x: list(map(lambda y:int(y),x)),s_list))
    #[['2'], ['2', '1'], ['2', '1', '3'], ['2', '1', '3', '4']] -> [[2], [2, 1], [2, 1, 3], [2, 1, 3, 4]]

    s_list.sort(key=len)


    answer = []
    answer.append(s_list[0][0])
    for i,j in zip(s_list[:-1],s_list[1:]):
        answer.append(set(j).difference(i).pop())

    return answer


ss = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
ss2 = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(ss2))
