#https://programmers.co.kr/learn/courses/30/lessons/43164

'''
모든 공항은 알파벳 대문자 3글자로 이루어집니다.
주어진 공항 수는 3개 이상 10,000개 이하입니다.
tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
주어진 항공권은 모두 사용해야 합니다.
만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
-> ["ICN", "JFK", "HND", "IAD"]

[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
- > ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

'''
'''
def solution(tickets):
    routes = dict()

    for t in tickets:
        if(t[0] in routes):
            routes[t[0]].append(t[1])
        else:
            routes[t[0]] = [t[1]]
    #print(routes)

    for k in routes.keys():
        routes[k].sort(reverse=True)
    #print(routes)


    start = ["ICN"]
    answer = []

    while start:
        stack = start[-1]

        if stack not in routes or len(routes[stack]) == 0:
            answer.append(start.pop())
        else:
            start.append((routes[stack].pop()))

    return answer[::-1]
    
    
'''
