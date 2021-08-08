import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt_s = collections.Counter(s)

        for char in s:
            if cnt_s[char] == 1:
                return s.index(char)

        return -1