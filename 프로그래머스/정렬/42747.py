#https://programmers.co.kr/learn/courses/30/lessons/42747
# [3, 0, 6, 1, 5]	-> 3
# [1, 1, 1] -> 1
# [1000] - > 1
import collections
def solution(citations):
    citations = sorted(citations,reverse=True) # 정렬
    num_of_citation = len(citations)
    #print(citations)
    #answer = 1
    for i in range(num_of_citation):
        print(citations[i] - i)
        if(citations[i] - i <= 0):
            return i

    return num_of_citation

# print(solution([3, 0, 6, 1, 5]))
# print(solution([1,1,1]))
# print(solution([10000]))
# print(solution([6,6,6,6,6,1]))
# print(solution([12,11,10,9,8,1]))
#print(solution([4,4,4]))
print(solution([20,21,22,23]))
# tt = [3, 0, 6, 1, 5]
# tt = [1, 1000]
# tt= sorted(tt)
#
# counts = collections.Counter(tt)
# print(counts.values())