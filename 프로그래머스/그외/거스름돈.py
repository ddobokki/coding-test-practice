#https://programmers.co.kr/learn/courses/30/lessons/12907

def solution(n, money):
    answer = [1] + [0] * n

    for m in money:

        for i in range(m, n + 1):
            answer[i] = answer[i] + answer[i - m]

    return answer[n]