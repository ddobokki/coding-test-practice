import collections
import math
def solution(N, road, K):
    answer = [math.inf,0] + [math.inf for i in range(N-1)]
    path = collections.defaultdict(list)
    dist_map = [[math.inf]*(N+1) for _ in range(N+1)]

    for r in road:
        start, end, w = r
        path[start].append(end)
        path[end].append(start)
        if dist_map[start][end] > w:
            dist_map[start][end], dist_map[end][start] = w, w

    q = collections.deque([1])

    while q:
        start = q.popleft()
        end_list = path[start]

        for end in end_list:
            dist = answer[start] + dist_map[start][end]
            if dist < answer[end] and dist <= K:
                answer[end] = dist
                q.append(end)

    return len(answer) - answer.count(math.inf)


solution(5,	[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],	3)