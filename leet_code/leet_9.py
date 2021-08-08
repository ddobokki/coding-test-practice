class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        s = str(x)
        return s == s[::-1]

        # left, right = 0, len(s) - 1
        #
        # while left < right:
        #     if s[left] != s[right]
a = []
a.re