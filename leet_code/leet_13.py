class Solution:
    roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                    'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

    def romanToInt(self, s: str) -> int:
        ans = 0
        idx = 0
        while idx < len(s):
            char = s[idx]
            if idx + 1 < len(s):
                if char == 'I' and (s[idx + 1] == 'V' or s[idx + 1] == 'X'):
                    char += s[idx + 1]
                    idx += 1
                if char == 'X' and (s[idx + 1] == 'L' or s[idx + 1] == 'C'):
                    char += s[idx + 1]
                    idx += 1
                if char == 'C' and (s[idx + 1] == 'D' or s[idx + 1] == 'M'):
                    char += s[idx + 1]
                    idx += 1
            ans += self.roman_to_int[char]
            idx += 1

        return ans

    
