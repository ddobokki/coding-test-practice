class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n % 4 != 0 and n < 1:
            return False

        while n > 1:
            n /= 4

        if n == 1:
            return True
        else:
            return False

print(Solution().isPowerOfFour(2))