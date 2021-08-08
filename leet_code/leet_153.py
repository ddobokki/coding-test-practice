from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            #print(nums[left], nums[mid], nums[right])
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

print(Solution().findMin([2,2,2,0,1]))
print(Solution().findMin([4,5,6,7,0,1,2]))
print(Solution().findMin([1,2,3,4,5]))