def solution(n, costs):
    cost = 0
    parent = [i for i in range(n)]

    def union(x,y):
        x = find(x)
        y = find(y)
        if x < y:
            parent[y] = x
        else:
            parent[x] = y

    def find(x):
        if parent[x] == x:
            return x
        return find(parent[x])

    costs.sort(key=lambda x:x[2])
    cnt = 0
    for s,e,c in costs:
        if find(s) != find(e):
            union(s,e)
            cost += c
            cnt += 1
            if cnt == n + 1:
                return cost
    return cost



#solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])
solution(4,[[0,1,1],[2,3,8]])