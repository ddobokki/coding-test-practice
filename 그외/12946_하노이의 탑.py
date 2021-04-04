answer = []


def hanoi(n, start, end, help):
    if n == 1:
        answer.append([start, end])
        return

    else:
        hanoi(n - 1, start, help, end)
        hanoi(1, start, end, help)
        hanoi(n - 1, help, end, start)

def solution(n):

    hanoi(n,1,3,2)
    return answer
