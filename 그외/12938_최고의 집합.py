def solution(n, s):
    center = s // n
    if center > 0:
        return [center] * (n - (s % n)) + [center + 1] * (s % n)
    else:
        return[-1]
'''
곱이 최대가 될때는 최대한 비슷한 크기의 숫자들이 곱해질때 최대가 된다.
s를 n으로 나누고 (int형 계산) 나머지가 r이라면 s/n의 값의 나머지가 k라면 s/n + 1을 k만큼 추가하고
n - k 값은 s/n 값으로 리스트에 추가하면된다.

'''
print(solution(2,1))