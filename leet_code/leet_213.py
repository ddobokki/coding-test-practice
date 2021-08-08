from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        dp1 = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)-1):
            dp1.append(max(dp1[-1], nums[i] + dp1[-2]))

        dp2 = [nums[1], max(nums[1], nums[2])]

        for i in range(3, len(nums)):
            dp2.append(max(dp2[-1], nums[i] + dp2[-2]))

        return max(dp1[-1], dp2[-1])