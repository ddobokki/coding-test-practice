# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):

    stack = []

    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
            continue
        else:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])

    if not stack:
        return 1
    else:
        return 0

solution('baabaa')