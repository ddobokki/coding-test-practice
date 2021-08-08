#https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    both = lost.intersection(reserve)
    lost = lost.difference(both)
    reserve = reserve.difference(both)

    students = ['student']*n
    for l in lost:
        students[l-1] = 'lost'
    for r in reserve:
        students[r-1] = 'reserve'
    state = students[0]
    for i in range(1,len(students)):
        if(students[i] == 'student'):
            state = 'student'
            continue
        if(state != 'student' and state != students[i]):
            students[i-1] = 'student'
            students[i] = 'student'
            state = 'student'
        else:
            state = students[i]
    answer = 0
    for s in students:
        if(s == 'student' or s == 'reserve'):
            answer += 1
    return answer

'''
훔쳐지지도, 여분을 가지도 않은 학생을 'student' 말고 다르게 표현할 방법이 있을까?
아니면 체육복을 기준으로 훔쳐지면 -1, 여벌은 +1, 아무것도 아니면 0 으로 표현해도 괜찮을까?
'''