# https://programmers.co.kr/learn/courses/30/lessons/60058
def reverse(str):
    str_li = list(str)
    for i,s in enumerate(str_li):
        if s == "(":
            str_li[i] = ")"
        else:
            str_li[i] = "("
    return ''.join(str_li)

def is_balance_str(string):
    cnt_open = 0
    cnt_close = 0

    for s in string:
        if s == "(":
            cnt_open += 1
        if s == ")":
            cnt_close += 1
    if cnt_open == cnt_close:
        return True
    else:
        return False


def is_correct_str(string):
    if is_balance_str(string):
        if string[0] == "(" and string[-1] == ")":
            return True
    return False

def split_u_v(str):
    temp_p = ''
    u, v = '', ''
    for i, s in enumerate(str):
        temp_p += s
        if is_balance_str(temp_p):
            u, v = temp_p, str[i + 1:]
            break
    return u,v

def solution(p):
    answer = ''

    if p == '':
        return ''
    u, v = split_u_v(p)

    if is_correct_str(u):
        answer = u + solution(v)

        return answer
    else:
        temp = "(" + solution(v) + ")"
        u = u[1:-1]
        u = reverse(u)
        answer += temp + u
        return answer

print(solution("()))((()"))
print(solution("()()()"))