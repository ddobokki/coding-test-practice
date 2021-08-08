# from collections import deque
#
#
# def check(x1, y1, x2, y2, nx, ny, s ,maps):
#     if y1 == y2:
#         cur = 0
#     else:
#         cur = 1
#     if maps[ny][nx] == 1:
#         return False
#
#     if nx == x1 and ny == y1:
#         return False
#     if nx == x2 and ny == y2:
#         return False
#     if s == 2:
#         if cur == 0:  # 가로로 놓여있을때
#             if ny == y2:
#                 return True
#             elif ny - 1 == y2:  # 90도 위
#                 if maps[y1 - 1][x1] != 1:
#                     return True
#                 else:
#                     return False
#             elif ny + 1 == y2:  # 90도 아래
#                 if maps[y1 + 1][x1] != 1:
#                     return True
#                 else:
#                     return False
#
#         if cur == 1:  # 세로로 놓여있을때
#             if nx == x2:
#                 return True
#             elif nx - 1 == x2:  # 오른쪽으로 회전
#                 if maps[y1][x1 + 1] != 0:
#                     return True
#                 else:
#                     return False
#             elif nx + 1 == x2:  # 왼쪽으로 회전
#                 if maps[y1][x1 - 1] != 0:
#                     return True
#                 else:
#                     return False
#     if s == 1:
#         if cur == 0:  # 가로로 놓여있을때
#             if ny == y1:
#                 return True
#             elif ny - 1 == y2:  # 90도 위
#                 if maps[y2 - 1][x2] != 1:
#                     return True
#                 else:
#                     return False
#             elif ny + 1 == y1:  # 90도 아래
#                 if maps[y2 + 1][x2] != 1:
#                     return True
#                 else:
#                     return False
#
#         if cur == 1:  # 세로로 놓여있을때
#             if nx == x1:
#                 return True
#             elif nx - 1 == x1:  # 오른쪽으로 회전
#                 if maps[y2][x2 + 1] != 0:
#                     return True
#                 else:
#                     return False
#             elif nx + 1 == x1:  # 왼쪽으로 회전
#                 if maps[y2][x2 - 1] != 0:
#                     return True
#                 else:
#                     return False
#     return 0


def solution(maps):
    answer = 0

    dx = [1, -1, 0, 0]  # 순서대로 동, 서, 남, 북
    dy = [0, 0, 1, -1]

    visit = [[-1] * len(maps[0]) for _ in range(len(maps))]  # 거리 측정 및, 방문을 확인하는 visit 배열
    visit[0][0] = 0  # visit이 -1이면 아직 방문을 안했다는 뜻
    visit[0][1] = 0
    q = deque([[0, 0, 1, 0]])  # 0,0에서 시작

    while q:
        x1, y1, x2, y2 = q.popleft()  # q에서 현재 좌표를 꺼낸다.

        for i in range(4):
            nx, ny = x2 + dx[i], y2 + dy[i]  # 순서대로 동서남북의 좌표

            if (0 <= nx < len(maps[0])) and (0 <= ny < len(maps)) and ((visit[ny][nx] == -1) or
                                                                       visit[y2][x2]+1 < visit[ny][nx]):
                # visit[y2][x2]+1 <= visit[ny][nx]
                # 각 루프마다 동서남북으로 갈수 있는 곳인지 확인
                if check(x1, y1, x2, y2, nx, ny,2, maps):
                    visit[ny][nx] = visit[y2][x2] + 1  # 현재 visit이 거리이므로 다음칸은 visit에 1을 더한값이 이동한 거리
                    q.append([x2, y2, nx, ny])  # 다음 좌표를 q에 삽입
        for i in range(4):
            nx, ny = x1 + dx[i], y1+ dy[i]  # 순서대로 동서남북의 좌표

            if (0 <= nx < len(maps[0])) and (0 <= ny < len(maps)) and ((visit[ny][nx] == -1) or
                                                                       visit[y1][x1]+1 < visit[ny][nx]):
                # visit[y2][x2]+1 <= visit[ny][nx]
                # 각 루프마다 동서남북으로 갈수 있는 곳인지 확인
                if check(x2, y2, x1, y1, nx, ny,1, maps):
                    visit[ny][nx] = visit[y1][x1] + 1  # 현재 visit이 거리이므로 다음칸은 visit에 1을 더한값이 이동한 거리
                    q.append([x1, y1, nx, ny])  # 다음 좌표를 q에 삽입
    for v in visit:
        print(v)
    print()
    for m in maps:
        print(m)
    return visit[-1][-1]


print(solution([[0, 0, 0, 1, 1],
                [0, 0, 0, 1, 0],
                [0, 1, 0, 1, 1],
                [1, 1, 0, 0, 1],
                [0, 0, 0, 0, 0]]))
