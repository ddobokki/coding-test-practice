n = 4


def solution(n):
    answer = []

    li = [[0] * i for i in range(1, n + 1)]
    i, j = 0, 0
    loop = 1
    num = 1
    while n > 0:
        state = loop % 3
        if (state == 1):
            for k in range(n):
                li[i][j] = num
                if (k != n - 1):
                    i += 1
                    j += 0
                num += 1
            j += 1
        if (state == 2):
            for k in range(n):
                li[i][j] = num
                if (k != n - 1):
                    i += 0
                    j += 1
                num += 1
            i -= 1
            j -= 1
        if (state == 0):
            for k in range(n):
                li[i][j] = num
                if (k != n - 1):
                    i -= 1
                    j -= 1
                num += 1
            i += 1
            j += 0
        n -= 1
        loop += 1
    for arr in li:
        answer += arr

    # sum(b,[])
    return answer


