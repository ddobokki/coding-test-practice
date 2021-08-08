#https://programmers.co.kr/learn/courses/30/lessons/42628

import heapq
from collections import deque
def solution(operations):
    operations = deque(operations)
    heap = []
    reverse_heap = []
    insert_count = 0
    for i in range(len(operations)):
        operation = operations.popleft()
        if(operation.startswith("I")):
            heapq.heappush(heap,int(operation[2:])) # data insert
            heapq.heappush(reverse_heap,-1*int(operation[2:]))
            insert_count += 1
        elif(operation.startswith("D -1")):
            if(len(heap) > 0):
                heapq.heappop(heap) # min data pop
                insert_count -= 1
        else:
            if(len(reverse_heap) > 0):
                heapq.heappop(reverse_heap) # max data pop
                insert_count -= 1
    print(heap)
    print(reverse_heap)
    if(insert_count <= 0):
        return [0,0]
    elif(insert_count == 2):
        return [-1*heapq.heappop(reverse_heap),-1*heapq.heappop(reverse_heap)]
    else:
        return [-1*heapq.heappop(reverse_heap),heapq.heappop(heap)]


#print(solution(	["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]))