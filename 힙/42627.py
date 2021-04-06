# https://programmers.co.kr/learn/courses/30/lessons/42627


import heapq


def solution(jobs):
    ans, now, i = 0, 0, 0
    start = -1
    heap = []
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            ans += now - cur[1]
            i += 1
        else:
            now += 1
    return ans // len(jobs)


'''

실패 테스트 케이스 좀더 확인해볼것

'''
