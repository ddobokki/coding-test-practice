from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def two_sum(nums, target):
            ans = []
            left, right = 0, len(nums) - 1

            while left < right:
                s = nums[left] + nums[right]
                if s < target or (left > 0 and nums[left] == nums[left - 1]):
                    left += 1
                elif s > target or (right < len(nums) - 1 and nums[right] == nums[right + 1]):
                    right -= 1
                else:
                    ans.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
            return ans

        def k_sum(nums, target, k):
            ans = []
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return ans
            if k == 2:
                return two_sum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for _, sets in enumerate(k_sum(nums[i + 1:], target - nums[i], k - 1)):
                        ans.append([nums[i]] + sets)
            return ans

        nums.sort()
        return k_sum(nums, target, 4)


print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
