from collections import deque

def solution(bridge_length, weight, truck_weights):
    sec = 1
    bridge = deque([0]*bridge_length)
    total_weight = truck_weights[0]
    bridge.append(truck_weights.pop(0))
    bridge.popleft()
    while truck_weights:
        sec += 1
        total_weight -= bridge.popleft()
        if(total_weight + truck_weights[0] > weight):
            bridge.append(0)
        else:
            total_weight += truck_weights[0]
            bridge.append(truck_weights.pop(0))

    sec += bridge_length
    return sec


print(solution(2,	10,	[7,4,5,6]))
a = deque([1,2,3])
