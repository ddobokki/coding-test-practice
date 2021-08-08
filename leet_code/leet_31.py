from typing import List
import itertools


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >=0 and nums[i+1]<=nums[i]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >=0 and nums[j] <= nums[i]:
                j -= 1
            nums[i],nums[j] = nums[j],nums[i]

        left = i + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


# [1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]
Solution().nextPermutation([2,3,1])
