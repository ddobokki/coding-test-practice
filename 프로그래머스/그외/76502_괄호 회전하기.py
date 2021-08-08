import collections


def solution(s):
    answer = -1

    cnt = 0
    for i in range(0, len(s)):
        s_q = collections.deque(s)
        for j in range(0, i):
            s_q.append(s_q.popleft())

        stack = []
        for k in range(0, len(s)):
            p = s_q.popleft()
            if not stack:
                if not (p == '[' or p == '{' or p == '('):
                    break
                else:
                    stack.append(p)
                    continue
            if p == '[' or p == '{' or p == '(':
                stack.append(p)
                continue
            if p == "]":
                if stack.pop() == "[":
                    continue
                else:
                    break
            if p == '}':
                if stack.pop() == "{":
                    continue
                else:
                    break
            if p == ')':
                if stack.pop() == "(":
                    continue
                else:
                    break
        else:
            if not stack:
                cnt += 1

    return cnt


solution("[](){}")
#solution(")(")
