#https://programmers.co.kr/learn/courses/30/lessons/42584
from collections import deque

def solution(prices):
    '''
    변수이름을 l_i 보다 count로 하는게 괜찮았을 것 같다.
    '''
    q = deque(prices)
    lenth = len(prices)
    answer = []
    i = 0
    while q:
        cur_p = q.popleft()
        i = i+1 # q 다음의 인덱스
        l_i = 0
        for k in range(i,lenth):
            l_i = l_i + 1
            if(cur_p > prices[k]):
                break
        answer.append(l_i)
    return answer

'''
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer
    
깔끔한 풀이 list[i] 의 시간 복잡도는 O(k)인 것을 이용
'''
