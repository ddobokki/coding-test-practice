from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot_idx = nums.index(min(nums))

        left = 0
        right = max(0,pivot_idx - 1)

        #print(left, right)

        while left <= right:
            #print('in')
            mid_idx = (left + right) // 2
            #print(nums[mid_idx] == target)
            if nums[mid_idx] < target:
                left = mid_idx + 1
            elif nums[mid_idx] > target:
                right = mid_idx - 1
            else:
                return mid_idx


        left = pivot_idx
        right = len(nums) - 1
        while left <= right:
            #print('in')
            mid_idx = (left + right) // 2
            #print(nums[mid_idx] == target)
            if nums[mid_idx] < target:
                left = mid_idx + 1
            elif nums[mid_idx] > target:
                right = mid_idx - 1
            else:
                return mid_idx


        return - 1

print(Solution().search([1,3],3))
