#https://programmers.co.kr/learn/courses/30/lessons/12914
def solution(n):
    #12900_2xn 타일링과 완전히 같은 문제
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

    return d3 % 1234567