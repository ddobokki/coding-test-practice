import itertools

def solution(numbers):
    numbers_combi = list(itertools.combinations(numbers,2))
    sum_num = list(set(map(lambda x: x[0] + x[1],numbers_combi)))
    answer = sorted(sum_num)
    return answer

print(solution([2,1,3,4,1]))