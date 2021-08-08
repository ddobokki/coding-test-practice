#https://programmers.co.kr/learn/courses/30/lessons/42890

# def solution(relation):
#     cnt = 0
#     candidate_list = []
#     for x in range(len(relation[0])):
#         candidate_key = set()
#         for y in range(len(relation)):
#             #print(relation[y][x])
#             candidate_key.add(relation[y][x])
#         #print(candidate_key)
#         if len(candidate_key) == len(relation):
#             cnt += 1
#             candidate_list.append(x)
#     print(candidate_list)
#     print(cnt)
#     return 0

from collections import deque
from itertools import combinations


def solution(relation):
    n_row = len(relation)
    n_col = len(relation[0])

    candidates = []
    for i in range(1, n_col + 1):
        candidates.extend(combinations(range(n_col), i))
    print(candidates)
    final = []
    for keys in candidates:
        tmp = [tuple([item[key] for key in keys]) for item in relation]
        if len(set(tmp)) == n_row:
            final.append(keys)
    print(final)
    answer = set(final[:])
    for i in range(len(final)):
        for j in range(i + 1, len(final)):
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])

    return len(answer)


solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],
          ["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])

