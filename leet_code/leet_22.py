from typing import List

import itertools
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        idx_open = list(itertools.combinations(list(range(2, 2*n)),n-1))
        ans = []
        idx_open.sort()
        for open in idx_open:
            p = "("
            for i in range(2, 2 * n):
                if i in open:
                    p += "("
                else:
                    p += ")"
            p += ")"
            if self.isValid(p):
                ans.append(p)
        return ans
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
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

print(Solution().generateParenthesis(3))
