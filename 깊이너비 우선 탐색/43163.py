# https://programmers.co.kr/learn/courses/30/lessons/43163
from collections import deque
def solution(begin, target, words):
    answer = 0
    Q = [begin]

    while True:
        temp_Q = [] # 큐 생성

        for word_1 in Q: # begin 단어부터 시작
            if word_1 == target: # 타겟 단어면 리턴
                    return answer
            for i in range(len(words)-1, -1, -1): # words 배열의 역순으로
                word_2 = words[i] # 단어 선택 비교를 위한 word2
                print(words)
                if sum([x!=y for x, y in zip(word_1, word_2)]) == 1: # 한글자만 다르면
                    temp_Q.append(words.pop(i)) # 단어를 큐에 넣는다, words에서 빼준다.
                    #print(temp_Q)
        if not temp_Q:
            return 0
        Q = temp_Q
        answer += 1

# 못품!

#(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))

#print(list(zip("hot", "dot")))