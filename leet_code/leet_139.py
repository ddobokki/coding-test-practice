from typing import List


class Solution:
    condi = False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def dfs(c,sub_s, word):
            if self.condi:
                return
            sub_s += word
            if sub_s in c:
                self.condi = self.condi or False
                return
            else:
                c.append(sub_s)

            if s[:len(sub_s)] != sub_s:
                # print(s[:len(sub_s)])
                # print(sub_s)
                self.condi = self.condi or False
                return

            if sub_s == s:
                self.condi = True
                return

            for w in wordDict:
                # print(len(sub_s))
                dfs(c,sub_s[:], w)

        check = []
        for i in wordDict:
            # print(i)
            dfs(check,'', i)

        return self.condi


print(Solution().wordBreak(s = "leetcode", wordDict = ["leet","code"]))
print(Solution().wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))

print(Solution().wordBreak(
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    , ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))

a = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
b = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]

# print(set(a).difference(set(''.join(b))))
