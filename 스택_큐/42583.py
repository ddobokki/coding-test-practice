import collections
def transfer(in_list, out_list):
    if(len(out_list) != 0):
        in_list.append(out_list.popleft())
    return 0
def next_weight(truck_weights):
    if(len(truck_weights) != 0):
        next = truck_weights[0]
    else:
        next = 0
    return next
def solution(bridge_length, weight, truck_weights):
    num_of_trucks = len(truck_weights)
    trucks = collections.deque(truck_weights)
    in_bridge = collections.deque()
    time_line = collections.deque()
    time = 1
    transfer(in_bridge, trucks)

    total_weight = in_bridge[0]
    time_line.append(1)
    while True:
        if (len(trucks) == 0):
            time = time + bridge_length
            break
        time = time + 1
        next = next = trucks[0]
        if((total_weight + next) <= weight and next != 0):
            total_weight = total_weight + next
            transfer(in_bridge, trucks)
            time_line.append(time)
        if(time - time_line[0] == bridge_length):
            total_weight = total_weight - in_bridge[0]
            in_bridge.popleft()
            if (total_weight + next) <= weight and next != 0:
                total_weight = total_weight + next
                transfer(in_bridge, trucks)
                time_line.append(time)
            time_line.popleft()
    answer = time
    return answer
# 실행시간 초과
'''
def solution(bridge_length, weight, truck_weights):
    q=[0]*bridge_length
    sec=0
    while q:
        sec+=1#시작했으므로 1초씩 더함
        q.pop(0)#트럭이 지나감
        if truck_weights:
            if sum(q)+truck_weights[0]<=weight:#다리에 있는 트럭의 무게와 대기 중인 트럭의 무게가 제한 무게보다 작거나 같다면
                q.append(truck_weights.pop(0))#다리에 트럭 올림
            else:
                q.append(0)#중량 초과면 트럭 안올림
    return sec
'''