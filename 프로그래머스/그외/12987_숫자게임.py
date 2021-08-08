# https://programmers.co.kr/learn/courses/30/lessons/12987
'''
정렬을 이용
A,B의 최댓값을 비교
A의 최댓값이 B의 최댓값보다 크면 어떠한 B의 요소도 이길 수 없으므로
A의 최댓값을 pop해준다(시간 복잡도 문제가 있으니 인덱스를 옮기는 것으로 대체)
B의 최댓값이 A의 최댓값보다 더 크면 카운트 해주고
B와 A의 최댓값을 pop해준다.

이것을 반복

'''


def solution(A, B):
    A = sorted(A, reverse=True)
    B = sorted(B, reverse=True)

    a_idx = 0
    b_idx = 0

    cnt = 0

    while a_idx < len(A) and b_idx < len(B):
        if A[a_idx] >= B[b_idx]:
            a_idx += 1
        else:
            cnt += 1
            a_idx += 1
            b_idx += 1
    return 0


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
print(solution([2,2,2,2],[1,1,1,1]))

'''
이전 코드, 정확성 통과 효율성 1/3

from collections import deque
def check_score(A,B):
    compare = list(map(lambda a,b: 1 if b>a else 0, A,B))
    return sum(compare)

def solution(A, B):
    answer = 0
    A.sort()
    B.sort()

    B = deque(B)

    score = [0]
    for _ in range(len(B)):
        s = check_score(A,B)
        if score[-1] <= s:
            score.append(s)
            B.append(B.popleft())
        else:
            break
    return score[-1]
'''
