
from math import factorial as f

def solution(n):
    #타일 1의 개수 -> n개
    #타일 2의 개수 -> n // 2개

    d1 = 1
    d2 = 2
    if n == 1:
        return d1
    if n == 2 :
        return d2


    for i in range(n - 2):
        d3 = d1 + d2
        d1 = d2
        d2 = d3

    return d3 % 1000000007

for i in range(1,10):
    print(i, ' ',solution(i))
