#https://programmers.co.kr/learn/courses/30/lessons/42586

'''

작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
작업 진도는 100 미만의 자연수입니다.
작업 속도는 100 이하의 자연수입니다.
배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다.
예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

progresses	speeds	return
[93, 30, 55]	[1, 30, 5]	[2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]

'''

from collections import deque
def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    complete_progresses = deque([])
    answer = []

    while(True): # 1 루프는 하루에 나타냄

        for i in range(len(progresses)):
            progress = progresses.popleft() # 작업의 진척도
            speed = speeds.popleft() # 작업의 속도
            progresses.append(progress+speed) # progresses 업데이트 큐의 가장 오른쪽에서 왼쪽으로 업데이트,
            speeds.append(speed) # pop된 speed를 다시 speeds의 가장 오른쪽에 넣어준다.

        if (progresses[0] >= 100): # 배포 우선순위가 높은 작업이 100 이상이면
            while(True):
                complete_progress = progresses[0]
                if(complete_progress >= 100):
                    complete_progresses.append(progresses.popleft()) # 배포될 작업으로 업데이트
                    speeds.popleft() # 작업이 끝났으므로 배포될 해당 progress의 speed도 빠져야한다.
                else:
                    break
                if(len(progresses) == 0): # 위의 작업으로 progresses의 큐가 0이면 루프를 빠져나간다.
                    break
        else:
            continue
        if(len(complete_progresses) != 0):
            answer.append(len(complete_progresses))
            complete_progresses.clear()

        if(len(progresses) == 0):
            break
    return answer

print(solution([93, 30, 55],[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99],	[1, 1, 1, 1, 1, 1]	))
print(solution([99, 1, 99, 1] ,[1, 1, 1, 1]))
print(solution([99, 98, 97] ,[1, 1,1]))