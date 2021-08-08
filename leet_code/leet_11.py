from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_a = 0
        while start < end:
            max_a = max(max_a, min(height[start],height[end]) * (end - start))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_a


# print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
print(Solution().maxArea([1, 0, 0, 0, 0, 0, 0, 2, 2]))
# print(Solution().maxArea([1,2,4,3]))
