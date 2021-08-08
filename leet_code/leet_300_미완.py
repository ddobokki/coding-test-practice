from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = 1
        max_ans = 1

        for i in range(1,len(dp)):
            max_val = 0
            for j in range(0,i):
                if nums[i] > nums[j]:
                    max_val = max(max_val,dp[j])

            dp[i] = max_val + 1
            max_ans = max(max_ans,dp[i])
        return max_ans
