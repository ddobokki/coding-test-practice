from itertools import combinations
def solution(numbers, target):
    answer = 0
    numbers_idx_li = range(len(numbers))
    for i in range(0,len(numbers) - 1):
        minus_num_idx = list(combinations(numbers_idx_li,i))

        for j in minus_num_idx:
            temp = 0
            for m_i,k in enumerate(numbers):
                if m_i in j:
                    temp -= k
                else:
                    temp += k
            if(temp == target):
                answer += 1

    return answer

# 0 -> 1, 1->n, 2->n^2


a = [1,1,1,1,1]
print(solution(a,3))