from typing import List

import collections
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_count = collections.Counter(nums2)

        intersect_list = []
        for n in nums1:
            if nums2_count[n] > 0:
                intersect_list.append(n)
                nums2_count[n] -= 1
        return intersect_list

print(Solution().intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))