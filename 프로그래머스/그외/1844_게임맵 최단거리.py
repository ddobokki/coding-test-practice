#https://programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque


def solution(maps):
    answer = 0

    dx = [1, -1, 0, 0]  # 순서대로 동, 서, 남, 북
    dy = [0, 0, 1, -1]

    visit = [[-1] * len(maps[0]) for _ in range(len(maps))]  # 거리 측정 및, 방문을 확인하는 visit 배열
    visit[0][0] = 1  # visit이 -1이면 아직 방문을 안했다는 뜻, 탐색이 끝나고도 도달 못하면 -1을 리턴해야하므로 -1로 초기화
    q = deque([(0, 0)])  # 0,0에서 시작

    while q:
        x, y = q.popleft()  # q에서 현재 좌표를 꺼낸다.

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]  # 순서대로 동서남북의 좌표

            if (0 <= nx < len(maps[0])) and (0 <= ny < len(maps)):  # 각 루프마다 동서남북으로 갈수 있는 곳인지 확인
                if (maps[ny][nx] == 1) and (visit[ny][nx] == -1):
                    # 갈수 있는 조건 -> 맵 밖이 아니고, visit하지 않았으며 맵이 1이어야 한다.
                    visit[ny][nx] = visit[y][x] + 1  # 현재 visit이 거리이므로 다음칸은 visit에 1을 더한값이 이동한 거리
                    q.append((nx, ny))  # 다음 좌표를 q에 삽입

    return visit[-1][-1]

#map = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]

#print(solution(map))
