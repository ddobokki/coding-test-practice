class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        stack.append(-1)
        for i in range(len(s)):
            print(ans)
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])

        return ans


Solution().longestValidParentheses("(())")
Solution().longestValidParentheses("()()")