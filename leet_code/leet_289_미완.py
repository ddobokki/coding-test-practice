class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        p_to_s = {}
        s_to_p = {}

        s_list = s.split()

        if len(pattern) != len(s_list):
            return False

        for i in range(len(pattern)):
            if not pattern[i] in p_to_s:
                p_to_s[pattern[i]] = s_list[i]
            else:
                if p_to_s[pattern[i]] != s_list[i]:
                    return False
            if not s_list[i] in s_to_p:
                s_to_p[s_list[i]] = pattern[i]
            else:
                if s_to_p[s_list[i]] != pattern[i]:
                    return False

        return True

print(Solution().wordPattern(pattern = "abba", s = "dog cat cat dog"))
print(Solution().wordPattern(pattern = "aaaa", s = "dog cat cat dog"))
print(Solution().wordPattern(pattern = "abba", s = "dog cat cat fish"))
print(Solution().wordPattern(pattern = "abba", s = "dog dog dog dog"))