#https://programmers.co.kr/learn/courses/30/lessons/42746
import itertools
def solution(numbers):
    #str_list = list(map(lambda e: str(e), numbers))
    permutation_list = list(itertools.permutations(numbers,len(numbers)))
    print(permutation_list)
    permutation_list = list(map(lambda e: ''.join(map(str,e)),permutation_list))
    permutation_list.sort()
    answer = permutation_list[-1]
    return answer

print(solution([6,10,2]))
#b = list(map(lambda e: str(e),a))
