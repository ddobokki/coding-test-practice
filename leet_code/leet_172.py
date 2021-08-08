import math
class Solution:


    def trailingZeroes(self, n: int) -> int:
        f = str(math.factorial(n))
        f = f[::-1]

        idx = 0
        cnt = 0
        while idx < len(f):
            if f[idx] == '0':
                cnt += 1
            else:
                break
            idx += 1
        #print(cnt)
        return cnt

Solution().trailingZeroes(7)
