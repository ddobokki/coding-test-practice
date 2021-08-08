from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, 1

        while left < right < len(nums):
            if nums[left] == nums[right]:
                left += 3
                right = left + 1
            else:
                return nums[left]
        return nums[left]
print(Solution().singleNumber([0,1,0,1,0,1,99]))
# 000 111 9