from typing import List

import collections
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums,reverse=True)
        #print(nums)
        c = collections.Counter(nums)
        idx = 0
        while k > 0:
            #print(nums[idx], k)
            k -= c[nums[idx]]
            if k <= 0:
                return nums[idx]
            idx += c[nums[idx]]
        return nums[idx]

print(Solution().findKthLargest([3,2,1,5,6,4],2))
print(Solution().findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))