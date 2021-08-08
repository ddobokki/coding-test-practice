# https://programmers.co.kr/learn/courses/30/lessons/49189
import collections
def solution(n, vertex):
    answer = 0
    dists = {i: 0 for i in range(1, n + 1)}
    #print(dists)
    edge = collections.defaultdict(list)

    for v, u in vertex:
        edge[v].append(u)
        edge[u].append(v)
    print(edge)
    q = collections.deque(edge[1])
    dist = 1
    loop = 1
    while q:
        #print(loop, ':' , q)
        for i in range(len(q)):
            v = q.popleft()
            #print(loop, ':', v)
            if(dists[v] == 0):
                dists[v] = dist
                for w in edge[v]:
                    q.append(w)
                print(loop,'  ', q, dists)
        dist += 1

        loop += 1
    del dists[1]

    max_value = max(dists.values())

    answer = 0

    for v in dists.values():
        if v == max_value:
            answer += 1
    return answer





solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])








# visit = [False] * (n + 1)
#
# def bfs(i,vertex):
#     if visit[i] == True:
#         return
#
#     visit[i] = True
#
#     for g_x in range(1,len(graph)):
#         for g_y in range(1,len(graph[g_x])):
#             if(graph[g_x][g_y] == 1):
#                 bfs(g_y,vertex)
#     return
#
# print(bfs(1,vertex))
