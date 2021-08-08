'''
scoville의 길이는 2 이상 1,000,000 이하입니다.
K는 0 이상 1,000,000,000 이하입니다.
scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
'''
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    min_sco1 = heapq.heappop(scoville) # 가장 작은 스코빌을 pop
    while (min_sco1 < K): # 가장 작은게 작으면 더해줌
        print(scoville)
        if (len(scoville) == 0):
            return -1
        min_sco2 = heapq.heappop(scoville) # 두번째 작은 스코빌을 pop
        heapq.heappush(scoville, min_sco1 + min_sco2 * 2) # 섞어주고 리스트에 추가
        answer = answer + 1 # 루프 1회
        min_sco1 = heapq.heappop(scoville) # 새로운 리스트에서 가장 작은 스코빌을 구함
    return answer

a = [2,1,454,234,123123,346]

heapq.heapify(a)

print(a)