def solution(n):

    if n == 0:
        return 0
    if n == 1:
        return 1

    fibo1 = 0
    fibo2 = 1
    fibo = fibo1 + fibo2
    for i in range(2,n):
        fibo1 = fibo2
        fibo2 = fibo
        fibo = fibo1 + fibo2

    return fibo % 1234567


'''
실제로 통과했던 코드

이게 되네;;;;

from functools import lru_cache
import sys
sys.setrecursionlimit(1000000)

@lru_cache(maxsize = 128)
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


def solution(n):
    answer = fibo(n) % 1234567
    return answer
    

'''

