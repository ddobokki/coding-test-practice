from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = strs[0]
        for string in strs:
            for i in range(0,min(len(ans),len(string))):
                if ans[i] != string[i]:
                    ans = ans[0:i]
                    break
            else:
                ans = ans[0 : min(len(ans),len(string))]

            if ans == "":
                break
        return ans

print(Solution().longestCommonPrefix(["dog","racecar","car"]))
print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix(["ab", "a"]))