import math
def lcm(a,b):
    return a*b//math.gcd(a,b)

def solution(arr):
    answer = 0

    lcm_li = []
    num1 = arr.pop(0)
    num2 = arr.pop(0)
    lcm_li.append(lcm(num1,num2))
    while arr:
        num3 = arr.pop(0)
        lcm_li.append(lcm(lcm_li[-1],num3))

    return lcm_li[-1]