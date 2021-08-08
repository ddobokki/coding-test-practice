#https://programmers.co.kr/learn/courses/30/lessons/42587

'''
현재 대기목록에는 1개 이상 100개 이하의 문서가 있습니다.
인쇄 작업의 중요도는 1~9로 표현하며 숫자가 클수록 중요하다는 뜻입니다.
location은 0 이상 (현재 대기목록에 있는 작업 수 - 1) 이하의 값을 가지며 대기목록의 가장 앞에 있으면 0, 두 번째에 있으면 1로 표현합니다.


priorities	location	return
[2, 1, 3, 2]	2	1
[1, 1, 9, 1, 1, 1]	0	5

'''
from collections import deque
def find_max_priorities(arr):
    max_priorities = arr[0][1]
    for i in range(1,len(arr)):
        next_prioriteies = arr[i][1]
        if(next_prioriteies >= max_priorities):
            max_priorities = arr[i][1]

    return max_priorities

def solution(priorities, location):
    priorities = list(map(lambda index, x: (index, x), range(len(priorities)), priorities))
    #priorities = list(map(lambda index, x: (index, x), enumerate(priorities)))
    priorities = deque(priorities)

    print_num = 0
    while(True):
        document = priorities.popleft()
        if(len(priorities) == 0):
            print_num += 1
            break
        max_priorities = find_max_priorities(priorities)
        if(document[1] < max_priorities):
            priorities.append(document)
        else:
            print_num += 1
            if(document[0] == location):
                break
    answer = print_num




    return answer

#print(solution(	[2, 1, 3, 2], 2))
#print(solution([4,3,2,1],3))


'''
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
                
다른 사람의 풀이

any를 활용,

enumerate를 사용했으면
list(map(lambda index, x: (index, x), range(len(priorities)), priorities)) 를
좀더 짧게 바꿀수 있었을것


'''