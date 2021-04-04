# https://programmers.co.kr/learn/courses/30/lessons/12909

# 60058에서 괄호를 이용하는 문제가 있었다. 여기에서 사용한 함수를 사용
import collections


def is_balance_parentheses(string):
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


def is_correct_parentheses(string):
    parentheses_q = collections.deque(list(string))
    q1 = collections.deque()
    if is_balance_parentheses(string):

        if string[0] == "(" and string[-1] == ")":
            for i in range(len(parentheses_q)):

                if not q1:
                    q1.append(parentheses_q.popleft())
                else:
                    if q1[-1] == "(" and parentheses_q[0] == ")":
                        q1.pop()
                        parentheses_q.popleft()
                    else:
                        q1.append(parentheses_q.popleft())
        else:
            return False
    else:
        return False
    if not q1:
        return True
    else:
        return False


def solution(s):
    return is_correct_parentheses(s)


#print(solution("())))(((()"))
#print(solution("()()()()()()()()()()"))
print(solution("((()"))
