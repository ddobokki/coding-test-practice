from typing import List


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         #print(nums)
#         ans = []
#         for i in range(len(nums) - 2):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             e1 = nums[i]
#             left = i + 1
#             right = len(nums) - 1
#             append_num = 0
#             while left < right < len(nums):
#                 e2 = nums[left]
#                 e3 = nums[right]
#                 if e1 + e2 + e3 == 0:
#                     ans.append((e1, e2, e3))
#                     append_num += 1
#                     left = i + append_num + 1
#                     right = right - 1
#                 elif e1 + e2 + e3 < 0:
#                     left += 1
#                 else:
#                     right -= 1
#
#         return list(set(ans))

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #print(nums)
        ans = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums) - 1

            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ < 0:
                    left += 1
                elif sum_ > 0:
                    right -= 1
                else:
                    ans.append([nums[i],nums[left],nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return ans

