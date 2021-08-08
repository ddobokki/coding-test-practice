import collections

def solution(n, edge):
    answer = 0
    graph = collections.defaultdict(list)

    for v, u in edge:
        graph[v].append(u)
        graph[u].append(v)

    visit = [False] * n
    q = collections.deque([])
    q.append([1,graph[1]])
    visit[0] = True
    dist_dict = {1 : 0}
    while q:
        cur_node , next_nodes = q.popleft()

        for next_node in next_nodes:
            if not visit[next_node-1]:
                q.append([next_node,graph[next_node]])
                visit[next_node - 1] = True
                if not next_node in dist_dict:
                    dist_dict[next_node] = dist_dict[cur_node] + 1

    max_dist = max(dist_dict.values())

    return list(dist_dict.values()).count(max_dist)

solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
