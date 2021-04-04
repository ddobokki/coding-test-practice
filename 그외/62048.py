#https://programmers.co.kr/learn/courses/30/lessons/62048
#멀쩡한 사각형
import math
def solution(w,h):
    if(w == h):
        return w*h - w
    elif(w == 1 or h == 1):
        return 0


    total = w * h
    gdc_of_wh = math.gcd(w,h)
    nh = h // gdc_of_wh
    nw = w// gdc_of_wh
    next_p = 0
    loss = 0
    for i in range(1,nw+1):
        cur_p = (nh / nw) * i
        loss += math.ceil(cur_p - next_p)
        next_p = math.floor(cur_p)

    return total - loss * gdc_of_wh

'''
연산 안해도 되는 두가지 경우(정사각형, 가로나 세로가 1일때는 if로 빼는게 중요

'''
print(solution(3,11))
print(solution(8,12))