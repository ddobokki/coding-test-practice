from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        left,right = 0,1
        cnt = 0
        #print(nums)
        while right < len(nums):
            #print(nums[right],cnt)
            if nums[left] == nums[right]:
                right += 1
                cnt += 1
            else:
                if cnt == 0:
                    return nums[left]

                left = right
                right += 1
                cnt = 0

        return nums[left]

print(Solution().singleNumber([4,1,2,1,2]))
print(Solution().singleNumber([1]))
print(Solution().singleNumber([2,2,1]))