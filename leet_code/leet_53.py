from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        temp_max = nums[0]
        for i in range(1, len(nums)):
            temp_max = max(nums[i],temp_max+nums[i])
            ans = max(temp_max,ans)
            
        return ans

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution().maxSubArray([-1,0,-2]))
#Solution().maxSubArray([5,4,-1,7,8])