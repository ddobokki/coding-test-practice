from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        diff = float('inf')
        for i in range(len(nums)):
            left,right = i + 1, len(nums) - 1
            while left < right:
                sum_ = nums[i] + nums[left]+ nums[right]
                if(abs(target - sum_)) < abs(diff):
                    diff = target - sum_
                if sum_ < target:
                    left += 1
                else:
                    right -=1

                if diff == 0:
                    break

        return target - diff

print(Solution().threeSumClosest( [-1,2,1,-4],2))


