from typing import List

import collections
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_count = collections.Counter(nums)

        for n in nums_count:
            while nums_count[n] > 1:
                nums.remove(n)
                nums_count[n] -= 1

        return len(nums)

Solution().removeDuplicates([1,1,2])

a = [1,1,2]
a[0] = None
print(a)