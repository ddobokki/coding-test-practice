import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_c = collections.Counter(magazine)

        for key in ransomNote:
            if not key in m_c:
                return False
            else:
                if m_c[key] > 0:
                    m_c[key] -= 1
                else:
                    return False
        return True


print(Solution().canConstruct("aa","ab"))