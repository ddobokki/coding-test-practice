class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]*(n+1)
        ps = [i*i for i in range(1,int(n**0.5)+1)]

        for i in range(1, int(n**0.5)+1):
            dp[i*i] = 1
        for i in range(1,n+1):
            if dp[i] == 1:
                continue
            dp[i] = dp[i-1] + 1
        for i in range(2,n+1):
            if dp[i] == 1:
                continue

            find_min = dp[i]
            for p in ps:
                if i - p >= 0:
                    find_min = min(find_min,dp[i-p] + 1)
                else:
                    break
            dp[i] = find_min


        return dp[n]

Solution().numSquares(13)
