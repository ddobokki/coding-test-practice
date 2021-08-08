import collections
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        idx = 0
        iso1 = collections.defaultdict(list)
        iso2 = collections.defaultdict(list)

        for i in range(len(s)):
            iso1[s[i]].append(t[i])
            iso2[t[i]].append(s[i])

        for i in iso1:
            if len(set(iso1[i])) != 1:
                return False
        for i in iso2:
            if len(set(iso2[i])) != 1:
                return False

        return True


print(Solution().isIsomorphic("bbbaaaba", "aaabbbba"))
print(Solution().isIsomorphic("badc",'baba'))
print(Solution().isIsomorphic("egg",'add'))