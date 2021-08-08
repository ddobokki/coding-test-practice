class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        d = 1
        for i in range(len(columnTitle)-1,-1,-1):
            num += (ord(columnTitle[i]) - ord('A') + 1) * d
            d *= 26
        return num
Solution().titleToNumber("ZY")