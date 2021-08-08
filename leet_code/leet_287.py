from typing import List

import collections
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_dict = collections.defaultdict(int)

        for n in nums:
            if nums_dict[n] == 0:
                nums_dict[n] += 1
            elif nums_dict[n] == 1:
                return n

'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            idx = abs(nums[i])-1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
            else:
                return abs(idx+1)
        return 0
공간복잡도 O(1), 시간복잡도 O(n)
가장 베스트 풀이인듯듯

'''