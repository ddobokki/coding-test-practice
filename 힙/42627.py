#https://programmers.co.kr/learn/courses/30/lessons/42627


import heapq
def solution(jobs):
    answer = 0
    jobs = sorted(jobs, key=lambda x: (x[0],x[1]))
    jobs = list(map(lambda x:(x[1],x[0]),jobs))
    schedule = jobs.copy()
   # print(schedule)
    processing = []
    last_work_time = 0
    #print(schedule)
    for j in range(len(jobs)):
        if(j == 0):
            processing.append(schedule.pop(0))
            continue
        last_work_time += processing[-1][0] # 작업이 끝나는 시간
        #print(last_work_time)
        #print(schedule)
        short_than_last_time = len(schedule)
        for s in range(len(schedule)):
            if(schedule[s][1] > last_work_time):
                short_than_last_time = s+1
                break
        #print(schedule[0:short_than_last_time])
        temp_heapq = schedule[0:short_than_last_time]
        heapq.heapify(temp_heapq)
        temp = heapq.heappop(temp_heapq)
        # 슬라이싱을 하면 깊은 복사가 되어버린다.
        schedule.pop(schedule.index(temp))
        processing.append(temp)
    task_complete_time = 0
    for p in processing:
        if(p[1] >= task_complete_time):
            task_complete_time = p[0] + p[1]
            answer = answer + task_complete_time - p[1]
        else:
            task_complete_time = task_complete_time + p[0]
            answer = task_complete_time + p[0]
        #print(task_complete_time)


    return int(answer/len(jobs))

#print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[1,1] , [25,1]]))
'''

실패 테스트 케이스 좀더 확인해볼것

'''