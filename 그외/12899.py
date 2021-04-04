# https://programmers.co.kr/learn/courses/30/lessons/12899


def solution(n):
    list_124 = ["4", "1", "2"]
    ans = ""
    while n > 0:
        remainder = int(n % 3)
        n //= 3

        if remainder == 0:
            n -= 1
        ans = list_124[remainder] + ans

    return ans


print(solution(1))
