from itertools import permutations
import math
def solution(n, k):
    total_list = list(range(1, n+1))
    answer = []
    i = k
    while n > 0:
        change = math.factorial(n - 1) # 횟수만큼 바뀌고
        answer.append(total_list.pop((i-1) // change))
        i = k % change
        n -= 1

    #answer.append(total_list.pop(0))
    return answer

print(list(permutations([1,2,3],3)))
print(solution(3,6))

# 총 경우의 수 k!
# 첫번째 숫자는 (k-1)! 마다 변환
# 두번째 숫자는 (k-2)! 마다 변환
# 7 -> 3! 2! + 1%
# 첫번째 자리 변환,