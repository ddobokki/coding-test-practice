#https://programmers.co.kr/learn/courses/30/lessons/43236
import itertools
def solution(distance, rocks, n):
    answer = 0
    rocks = sorted(rocks)
    rocks.append(n)
    short_dist = []

    cur = 0
    for i in rocks[:-1]:
        short_dist.append(i - cur)
        cur = i
    print(short_dist)
    return answer


solution(25,[2, 14, 11, 21, 17],2)