from typing import List

import collections
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        color_cnt = collections.Counter(nums)
        print(color_cnt)
        idx = 0

        for i in range(color_cnt[0]):
            nums[idx] = 0
            idx += 1
        for i in range(color_cnt[1]):
            nums[idx] = 1
            idx += 1
        for i in range(color_cnt[2]):
            nums[idx] = 2
            idx += 1

        print(nums)
