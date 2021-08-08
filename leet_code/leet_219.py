from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idx_dict = {}

        for i in range(len(nums)):
            if not nums[i] in idx_dict:
                idx_dict[nums[i]] = i
            else:
                if abs(i - idx_dict[nums[i]]) <= k:
                    return True
                else:
                    idx_dict[nums[i]] = i
        return False
