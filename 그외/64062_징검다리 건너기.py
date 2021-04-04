from collections import deque
import heapq


def change_stones(li, s):  # n번째 사람이 지나갈 때의 돌의 상황
    return list(map(lambda x: 0 if x < s else x, li))


# def check(li, s ,k):
#     for i in range(len(li)):
#         if li[i] < s and i + k - 1 < len(li):
#             cnt = 0
#             for j in range(k):#li[i:i+k]: # 0,0,0 이 있으면 False를 리턴
#                 if li[i+j] < s:
#                     cnt += 1
#                 else:
#                     break
#             if cnt == k:
#                 return False
#             # if not any(li[i:i + k]):
#             #     return False
#     return True
def check(li,s,k):
    cnt = 0
    for i in range(len(li)):

        if li[i] < s and i + k - 1 < len(li):
            cnt += 1
        else:
            cnt = 0
        if cnt == k:
            return False
    return True

def solution(stones, k):
    min_s = 1
    max_s = max(stones)
    mid_s = 0

    while min_s <= max_s:
        mid_s = (min_s + max_s) // 2
        if check(stones, mid_s ,k):  # 지나갈 수 있으면 더 지나갈수 있나 확인
            answer = mid_s
            min_s = mid_s + 1

        else:
            max_s = mid_s - 1

    return answer


#
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
print(change_stones([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))
#print(check([1, 0, 0, 0, 0, 1], 5))
# print(solution([1,1,1,1,5,1,1,1,1], 6))

# def check(li, k):  #
#     cnt = 1
#     li = sorted(li)
#     l = li[0]
#     for i in range(1, len(li)):
#         if l + cnt == li[i]:
#             cnt += 1
#             if cnt == k:
#                 return True
#         else:
#             l = li[i]
#             cnt = 1
#     return False
#
#
# def solution(stones, k):
#     # 루프를 돌며 1을 뺀다
#     # 0이 추가될때마다 확인
#     loop = 0
#     while True:
#         zero_idx = []
#         for i in range(len(stones)):
#             stone = stones[i]  # 인덱스 i의 스톤
#
#             if stone == 0:
#                 zero_idx.append(i)
#                 if check(zero_idx,k):
#                     return loop
#                 continue
#             else:
#                 stones[i] = stone - 1
#         loop += 1


# print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
# print(solution([2, 4, 5, 3, 2, 1, 4, 0, 0, 0], 3))
# print(check([1, 2, 4, 5, 6,7], 5))
