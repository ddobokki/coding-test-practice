#https://programmers.co.kr/learn/courses/30/lessons/49191
import collections
def solution(n, results):
    results_dict ={i: 0 for i in range(1,n + 1)} # 1번선수 부터 n+1번선수가 패배한 횟수
    total_game = n - 1
    edge = collections.defaultdict(list)
    win_game = [0]*(n+1)
    for win_num,lose_num in results:
        edge[win_num].append(lose_num)

    for player in range(1,n+1):
        q = collections.deque(edge[player])
        visit = [False] * (n + 1)
        loop = 0
        while q:

            for i in range(len(q)):
                next_g = q.popleft()
                if(visit[next_g] == False):
                    visit[next_g] = True
                    loop += 1
                    results_dict[next_g] += 1 # 그래프의 도착하게 되면, 이전 그래프의 선수에게 패배했단 뜻

                    for l in edge[next_g]:
                        q.append(l)
        win_game[player] = loop
    answer = 0
    for player_num in range(1,n+1):
        if(win_game[player_num] + results_dict[player_num] == total_game):
            answer += 1
    print(results_dict)
    print(win_game[1:n+1])
    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
print(solution(4,[[4,3],[3,2],[2,1]]))
print(solution(4,[[4,3],[4,2],[4,1]]))
# a = [True]*5
# a.append(False)
# print(all(a[0:4]))
'''
# https://programmers.co.kr/learn/courses/30/lessons/49189 는 못풀었지만
참고한 코드를 바탕으로 풀었다.

'''