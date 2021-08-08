import bisect
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]

        i = bisect.bisect_left(nums,target)
        j = bisect.bisect_right(nums,target)

        if i < 0 or i > len(nums) - 1:
            return [-1, -1]


        if nums[i] != target:
            return [-1,-1]
        else:
            return [i, j - 1]

print(Solution().searchRange( [2,2],3))