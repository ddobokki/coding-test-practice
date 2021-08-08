from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        idx = 0
        while idx < len(nums):
            if idx != nums[idx]:
                return idx

            idx += 1
        return idx
