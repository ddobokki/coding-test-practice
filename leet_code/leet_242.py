class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return ''.join(sorted(s)) == ''.join(sorted(t))

print(Solution().isAnagram(s = "anagram", t = "nagaram"))