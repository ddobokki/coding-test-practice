import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        x = 0
        while True:
            if 3**x == n:
               return True

            if 3**x < n:
                x += 1
            elif 3**x > n:
                return False


print(Solution().isPowerOfThree(45))
