# https://programmers.co.kr/learn/courses/30/lessons/12941
# 한 배열의 최솟값과 다른 배열의 최댓값을 곱하면 최종적으로 최솟값을 가지는 배열이 리턴

import heapq as hq

def solution(A, B):
    hq.heapify(A)

    B = list(map(lambda x: -x, B))
    hq.heapify(B)
    answer = 0
    for i in range(len(A)):
        answer += hq.heappop(A) * (hq.heappop(B)) * -1

    return answer


print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1, 2], [3, 4]))
