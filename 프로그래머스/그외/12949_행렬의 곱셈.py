# https://programmers.co.kr/learn/courses/30/lessons/12949
import numpy as np


def solution(arr1, arr2):
    #3중 포문을 쓰라는 문제지만 어림없지 넘파이
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    answer = (arr1 @ arr2).tolist()

    return answer
print(solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]]))