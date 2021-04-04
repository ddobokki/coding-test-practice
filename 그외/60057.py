# https://programmers.co.kr/learn/courses/30/lessons/60057

from collections import deque


def str_slice_by_n(s, n):
    # s_que = deque(list(s))
    # slice_s = []
    # while s_que:
    #     temp_s = []
    #     if len(s_que) < n :
    #         for i in range(len(s_que)):
    #             temp_s.append(s_que.popleft())
    #     else:
    #         for i in range(n):
    #             temp_s.append(s_que.popleft())
    #     slice_s.append(temp_s)

    idx = 0
    slice_s = []
    for i in range(len(s) // n + 1):
        temp_s = s[idx:idx + n]
        if len(temp_s) != 0:
            slice_s.append(s[idx:idx + n])
        idx = idx + n
    return slice_s


def str_compress(s_list):
    cur_str = s_list[0]
    cnt = 1
    compress_str = []
    for idx in range(1, len(s_list)):
        if cur_str == s_list[idx]:
            cnt += 1
        else:
            compress_str.append(str(cnt))
            compress_str.append(cur_str)
            cur_str = s_list[idx]
            cnt = 1
    compress_str.append(str(cnt))
    compress_str.append(cur_str)

    for i in range(len(compress_str)):
        if compress_str[i] == "1":
            compress_str[i] = ""
    return "".join(compress_str)


def solution(s):
    compressed_str_len = []
    if(len(s) == 1):
        return 1
    for i in range(1, len(s) // 2 + 1):
        compressed_str = str_compress(str_slice_by_n(s, i))
        compressed_str_len.append(len(compressed_str))


    return min(compressed_str_len)


print(solution("a"))

