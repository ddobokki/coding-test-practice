from typing import List


def solution(lottos:List, win_nums):
    zeros = lottos.count(0)
    correct = 0
    for lotto in lottos:
        if lotto != 0 and win_nums.count(lotto) != 0:
            correct += 1
    a = 7 - correct - zeros if 7 - correct - zeros != 7 else 6

    b = 7 - correct if 7 - correct != 7 else 6
    return [a, b]

print(solution([1,2,3,4,5,6],[10,11,12,13,14,15]))