dp = {}
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp[1] = 0
        def helper(n):
            if n in dp:
                return dp[n]
            if n % 2 == 0:
                dp[n] = helper(n/2) + 1
            else:
                dp[n] = min(helper(n-1), helper(n+1)) + 1
            return dp[n]
        helper(n)
        return dp[n]
print(Solution().integerReplacement(100))
