'''
N은 1 이상 9 이하입니다.
number는 1 이상 32,000 이하입니다.
수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
최솟값이 8보다 크면 -1을 return 합니다.

'''
import string

def solution(N, number):

    return a


using_str_add = []
using_str_add.append(0)
posiible_set = [0,[5]]
for i in range(1,8):
    using_str_add.append(int(str(5)*i))

temp_i = []
for i in range(2,3):
    temp_j = []
    for j in range(i):
        temp_j.append(posiible_set[j] + posiible_set[j - i])
        temp_j.append(posiible_set[j] - posiible_set[j - i])
        temp_j.append(posiible_set[j] * posiible_set[j - i])
        if(posiible_set[j-i] != 0):
            temp_j.append(posiible_set[j] / posiible_set[j - i])


print(temp_j)
