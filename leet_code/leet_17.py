from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                      '6': 'mno', '7': 'qprs', '8': 'tuv', '9': 'wxyz'}
        ans = []
        if len(digits) == 0:
            return []
        def dfs(c,n, k):
            if k == len(digits) - 1:
                for char in phone_dict[n]:
                    ans.append(c + char)
                return

            for char in phone_dict[n]:
                dfs(c+char,digits[k + 1], k + 1)

        dfs('',digits[0], 0)

        return ans
print(Solution().letterCombinations("2"))
