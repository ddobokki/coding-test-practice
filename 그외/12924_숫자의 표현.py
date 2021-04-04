#https://programmers.co.kr/learn/courses/30/lessons/12924

#
#
def solution(n):

    start = 1
    end = n
    mid = (start + end) // 2
    cnt = 0
    while start <= end // 2:

        num = (mid - start + 1)*(start + mid) // 2
        print(start, mid, num)
        if num > n:
            mid -= 1
        elif num < n:
            mid += 1
            start += 1
        else:
            cnt += 1
            start += 1

    cnt += 1
    return cnt


print(solution(15))