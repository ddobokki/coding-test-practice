def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x:x[2])
    connection = [costs[0][0]]
    print(costs)
    print(connection)

    while len(connection) != n:
        for i,cost in enumerate(costs):
            if(cost[0] in connection) and (cost[1] in connection) :
                continue
            if(cost[0] in connection or cost[1] in connection):
                answer += cost[2]
                connection.append(cost[0])
                connection.append(cost[1])
                connection = list(set(connection))
                costs.pop(i)
                break

    return answer

print(solution(4,	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))