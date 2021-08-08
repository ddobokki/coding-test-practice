from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, window_sum, min_length = 0, 0, len(nums) + 1
        for r in range(len(nums)):
            window_sum += nums[r]
            while window_sum >= target:
                window_sum -= nums[l]
                min_length = min(min_length, r - l + 1)
                l += 1
        return min_length if min_length <= len(nums) else 0
#print(Solution().minSubArrayLen(7,[2,3,1,2,4,3]))
print(Solution().minSubArrayLen(4,[1,4,4]))

