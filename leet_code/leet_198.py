from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [nums[0],max(nums[0],nums[1])]

        for i in range(2,len(nums)):
            dp.append(max(dp[-1],nums[i]+dp[-2]))
        print(dp)
        return dp[-1]
# Solution().rob([2,7,9,3,1])
# Solution().rob([1,2,3,1])
Solution().rob([1,1,1,1,1,1,1,1,1,1,1,1,1,100,1])