#https://programmers.co.kr/learn/courses/30/lessons/42579

import collections
'''
속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
'''
def solution(genres, plays):
    answer = []

    genres_idx = collections.defaultdict(list)
    genres_play = collections.defaultdict(int)

    for i,g in enumerate(genres):
        genres_idx[g].append((i,plays[i]))

    for g,play in zip(genres,plays):
        genres_play[g] = genres_play[g] + play

    play_sort = []
    for s in list(set(genres)):
        play_sort.append((s,genres_play[s]))
    play_sort = sorted(play_sort,reverse=True,key=(lambda x:x[1]))

    for g,p_n in play_sort:
        genres_idx[g] = sorted(genres_idx[g],reverse=True,key=(lambda x:x[1]))
        temp = list(map(lambda x:x[0],genres_idx[g][0:2]))
        for i in temp:
            answer.append(i)

    return answer


'''
변수명 날잡고 바꾸기

'''