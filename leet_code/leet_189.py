from typing import List

import collections
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # """
        # Do not return anything, modify nums in-place instead.
        # """
        # nums_d = collections.deque(nums)
        #
        # while k > 0:
        #     nums_d.appendleft(nums_d.pop())
        #     k -= 1
        # for i in range(len(nums)):
        #     nums[i] = nums_d.popleft()

        while k > 0:
            nums.insert(0,nums.pop())
            k -= 1