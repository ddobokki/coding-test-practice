#https://programmers.co.kr/learn/courses/30/lessons/42578

'''
clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
같은 이름을 가진 의상은 존재하지 않습니다.
clothes의 모든 원소는 문자열로 이루어져 있습니다.
모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
스파이는 하루에 최소 한 개의 의상은 입습니다.
'''

def dictionary_clothes_num(clothes):
    d = dict()

    for c in clothes:
        if c[1] in d.keys():
            d[c[1]] = d[c[1]] + 1
        else:
            d[c[1]] = 1

    return d
def solution(clothes):
    answer = 1
    clothes_dict = dictionary_clothes_num(clothes)
    for i in clothes_dict.values():
        answer = answer * (i+1)

    return answer - 1


