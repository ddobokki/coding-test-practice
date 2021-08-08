#https://programmers.co.kr/learn/courses/30/lessons/12911
def solution(n):
    num_one = format(n, 'b').count('1')

    return find(n + 1, num_one)


def find(n, num_one):
    bin_n = format(n, 'b')
    if bin_n.count('1') == num_one:
        return n
    else:
        return find(n + 1, num_one)


