from collections import deque
def solution(people, limit):
    answer = 0
    people = sorted(people)
    max_p = []

    right = 0
    left = len(people) - 1

    while right < left:
        if(people[right] + people[left] <= limit): # 보트에 들어가는 경우
            right += 1
            left -= 1
        else:
            left -= 1 # 큰거를 빼준다
        answer += 1
    if(right == left):
        answer += 1

    return answer

print(solution([10,10,10], 100))
