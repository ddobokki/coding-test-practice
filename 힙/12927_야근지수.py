import heapq


def solution(n, works):
    answer = 0
    works = list(map(lambda x: -1 * x, works))
    heapq.heapify(works)

    while works and n > 0:
        max_work = heapq.heappop(works)

        max_work += 1
        n -= 1
        if max_work != 0:
            heapq.heappush(works,max_work)

    if works:
        for w in works:
            answer += w ** 2
    else:
        answer = 0
    return answer


solution(4, [4, 3, 3])
solution(1, [2, 1, 2], )
solution(3, [1, 1])
"""
[4, 3, 3]	4	12
[2, 1, 2]	1	6
[1,1]	3	0
"""
