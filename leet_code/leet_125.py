class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        preprocess = ''
        for char in s:
            if char.isalpha() or char.isdigit():
                preprocess += char
        s = preprocess
        return s == s[::-1]
