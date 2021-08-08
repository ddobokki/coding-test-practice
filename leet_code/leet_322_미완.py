from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()

        dp = [[-1] * (amount + 1) for j in range(len(coins))]

        for i in range(len(coins)):
            coin = coins[i]
            for j in range(amount + 1):
                if j == 0:
                    dp[i][j] = 0
                if j % coin == 0:
                    dp[i][j] = j // coin


        #
        # for d in dp:
        #     print(d)
        # print()
        for i in range(len(coins)):
            coin = coins[i]
            cur_max = 0
            for j in range(amount + 1):

                if dp[i][j] != -1:
                    cur_max = dp[i][j]

                if dp[i][j] == -1 and i - 1 >= 0:
                    if j - coin < 0:
                        # if dp[i - 1][j] != -1:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        #print(i,j,  '-' ,cur_max, dp[i][j-coin])
                        if dp[i][j-cur_max*coin] != -1:
                            dp[i][j] = cur_max + dp[i][j-cur_max*coin]
                        else:
                            dp[i][j] = dp[i-1][j]

        for d in dp:
            print(d)

        return dp[-1][-1]

print(Solution().coinChange([186,419,83,408],6249))
#print(Solution().coinChange(coins = [1,2,5], amount = 11))
# print(Solution().coinChange([1],0))