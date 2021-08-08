# import collections
# def solution(a, edges):
#
#     if sum(a) != 0:
#         return -1
#
#     graph = collections.defaultdict(list)
#     weight = collections.defaultdict()
#
#     for u,v in edges:
#         graph[u].append(v)
#         graph[v].append(u)
#     for i,w in enumerate(a):
#         weight[i] = w
#
#     #print(top)
#     top = 2
#     # cur_len = 0
#     # for i in graph.keys():
#     #     if cur_len < len(graph[i]):
#     #         top = i
#     #         cur_len = len(graph[i])
#
#     #print(weight)
#
#     q = collections.deque([top])
#     visit = [False]*len(a)
#     last = []
#     while q:
#
#         cur = q.popleft()
#         visit[cur] = True
#
#         is_next = False
#         for next in graph[cur]:
#             if not visit[next]:
#                 q.append(next)
#                 is_next = True
#         if not is_next:
#             last.append(cur)
#
#     print(last)
#     visit = [False]*len(a)
#     next_visit = [False]*len(a)
#     q = collections.deque(last)
#     cnt = 0
#     while q:
#         print(q)
#         cur = q.pop()
#         visit[cur] = True
#         for next in graph[cur]:
#
#
#                 if weight[cur] >= 0:
#                     cnt += weight[cur]
#                     weight[next] += weight[cur]
#                     weight[cur] = 0
#                 else:
#                     cnt -= weight[cur]
#                     weight[next] -= weight[cur]
#                     weight[cur] = 0
#         graph[]
#
#     return cnt


import collections

def solution(a, edges):
    graph = collections.defaultdict(list)
    leaf_del_count = collections.defaultdict(int)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    leaf = collections.deque()
    visited = [False for _ in range(len(a))]
    total = 0

    for node in range(len(a)):
        total += a[node]
        if len(graph[node]) == 1:
            leaf.append(node)
    if total != 0: return -1

    ans = 0
    while leaf:
        node = leaf.popleft()
        visited[node] = True
        for next_node in graph[node]:
            # graph[next_node].remove(node)
            leaf_del_count[next_node] += 1
            if not visited[next_node]:
                if len(graph[next_node]) - leaf_del_count[next_node] == 1: leaf.append(next_node)
                if a[node]==0: continue
                ans += abs(a[node])
                a[next_node] += a[node]
                a[node] = 0
    return ans

print(solution(	[-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]))
#print(solution([0,1,0],	[[0,1],[1,2]]))