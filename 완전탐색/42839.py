# https://programmers.co.kr/learn/courses/30/lessons/42839
'''
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

numbers	return
"17"	3
"011"	2
'''
from itertools import permutations
def check_prime(n):
    if(n <= 1):
        return False
    i = 2
    while(i <= n**(0.5)):
        if(n % i == 0):
            return False
        i += 1
    return True


def solution(numbers):
    num_list = list(numbers)
    permu_list = []
    for i in range(1,len(num_list)+1):

        permu_list += list(permutations(num_list,i))


    numbers = set((map(lambda x: int(''.join(x)),permu_list)))
    answer = 0
    for num in numbers:
        if check_prime(num):
            answer += 1
    return answer

print(solution("011"))
# c = ["1","7"]
#
# print(list(permutations(c,2)))