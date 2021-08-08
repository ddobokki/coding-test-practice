import math

def solution(n,a,b):

    math_num = 1

    while True:
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        if abs(a - b) == 0:
            break
        math_num += 1

    return math_num

print(solution(8,1,2))
#2, 1,2 - >1
#4, 1,2 -> 1, 1,3 ->2
