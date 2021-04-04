# https://programmers.co.kr/learn/courses/30/lessons/68936

'''
[[1,1,0,0],
[1,0,0,0],
[1,0,0,1],
[1,1,1,1]]	[4,9]

[[1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,1],
[0,0,0,0,1,1,1,1],
[0,1,0,0,1,1,1,1],
[0,0,0,0,0,0,1,1],
[0,0,0,0,0,0,0,1],
[0,0,0,0,1,0,0,1],
[0,0,0,0,1,1,1,1]]	[10,15]
'''


def same_check(arr):  # 전부 같은 값이면 True
    temp_list = []
    for a in arr:
        temp_list += a
    if min(temp_list) == max(temp_list):
        return True
    else:
        return False


def divide_arr(arr):
    divide_len = len(arr) // 2
    arr_00 = []
    arr_01 = []
    arr_10 = []
    arr_11 = []
    for i, aa in enumerate(arr):
        if i < divide_len:
            arr_00.append(aa[0:divide_len])
            arr_01.append(aa[divide_len:])
        else:
            arr_10.append(aa[0:divide_len])
            arr_11.append(aa[divide_len:])

    return arr_00, arr_01, arr_10, arr_11


answer = []


def quad_compress(arr):
    if same_check(arr):
        answer.append(arr[0][0])
    else:
        if len(arr) > 1:
            a, b, c, d = divide_arr(arr)
            quad_compress(a)
            quad_compress(b)
            quad_compress(c)
            quad_compress(d)
    return 0


def solution(arr):
    quad_compress(arr)
    return [answer.count(0), answer.count(1)]


# print(solution([[1,1,0,0],
# [1,0,0,0],
# [1,0,0,1],
# [1,1,1,1]]))

aaa = solution([[1, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 1, 1, 1, 1],
                [0, 1, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 1, 1, 1, 1]])

print(aaa)
