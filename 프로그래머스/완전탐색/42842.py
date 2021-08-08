#https://programmers.co.kr/learn/courses/30/lessons/42842

def find_hight_width(block_num):
    hight_width = []
    for hight in range(1, int(block_num / 2) + 2):
        if (block_num % hight == 0):
            width = int(block_num / hight)
            if (hight <= width):
                hight_width.append([hight, width])
            else:
                break
    return hight_width
def solution(brown, yellow):
    y_hight_width = find_hight_width(yellow)

    for i,y in enumerate(y_hight_width):
        if(y[0] * 2 + y[1] * 2 + 4 == brown):
            break

    return [y_hight_width[i][1] + 2,y_hight_width[i][0] + 2]

'''
import math
def solution(brown, yellow):
    w = ((brown+4)/2 + math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    h = ((brown+4)/2 - math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    return [w,h]
    
근의 공식으로 푼 코드
관계식을 잘 찾으면 쉽게 풀 수 있었을듯

'''




#solution(24, 24)