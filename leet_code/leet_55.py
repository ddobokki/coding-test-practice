from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        left = 0
        right = len(nums) - 1

        if nums[left] == 0:
            return False

        while left < right:
            if nums[left] == 0:
                sub_left = left - 1
                while sub_left >= 0:
                    if nums[sub_left] + sub_left > left:
                        break
                    sub_left -= 1

                    if sub_left == -1:
                        return False

            left += 1


        return True

# print(Solution().canJump([3,2,1,0,4]))
# print(Solution().canJump([2,3,1,1,4]))
print(Solution().canJump([1,0,2]))