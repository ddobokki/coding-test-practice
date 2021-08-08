class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        exp = 0
        for i in range(1,n+1):
            front = 9
            r = 9
            for j in range(i - 1):
                front *= r
                r -= 1
            dp[i] = dp[i-1] + front
        return dp[-1]

Solution().countNumbersWithUniqueDigits(4)