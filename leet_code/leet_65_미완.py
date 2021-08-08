class Solution:

    def isNumber(self, s: str) -> bool:
        s = s.lower()
        if s.isdigit():
            return True
        if 'e' in s:
            if not s[s.index('e') + 1 :].isdigit():
                return False





a = "1.7"
print(a.isdigit())