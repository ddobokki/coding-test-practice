import collections


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = collections.deque()
        for p in s:
            if len(stack) == 0:  # 스택이 0 일때
                if p == "(" or p == "{" or p == "[":  # 해당 괄호가 오면 스택이 넣는다
                    stack.append(p)
                    continue
                else:  # 닫는 괄호가 오면 false
                    return False

            if p == "(" or p == "{" or p == "[":
                stack.append(p)

            if p == ")" or p == "}" or p == "]":
                parentheses = stack.pop()
                #print(parentheses)
                if parentheses == "(":
                    if not p == ")":
                        return False
                elif parentheses == "{":
                    if not p == "}":
                        return False
                elif parentheses == "[":
                    if not p == "]":
                        return False
        return not stack

print(Solution().isValid("()"))
print(Solution().isValid("(]"))
print(Solution().isValid("{[]}"))