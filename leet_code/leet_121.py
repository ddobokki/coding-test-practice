from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        profit = 0

        for p in prices:
            if not stack:
                stack.append(p)
                continue
            if p <= stack[-1]:
                stack.append(p)
                continue
            if p > stack[-1]:
                profit = max(profit,p - stack[-1])
        return profit
Solution().maxProfit([7,1,5,3,6,4])