from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                pointer = i
                while pointer < len(nums):
                    if nums[pointer] != 0:
                        nums[i], nums[pointer] = nums[pointer], nums[i]
                        break
                    pointer += 1

        print(nums)
Solution().moveZeroes([0,1,0,3,12])
Solution().moveZeroes([0])


