import math
def solution(n):
    answer = []
    divide = 10 ** int(math.log10(n))
    while divide != 0:
        answer.append(n // divide)
        n = n % divide
        divide = divide // 10
    answer.sort()
    ans = 0

    for i,num in enumerate(answer):
        ans += num * 10**i
    print(ans)
    return ans

solution(118372)