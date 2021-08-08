from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for idx, height in enumerate(heights + [0]):
            while stack and heights[stack[-1]] >= height:
                currHeight = heights[stack.pop()]
                width = idx if not stack else idx - stack[-1] - 1
                maxArea = max(maxArea, currHeight * width)

            stack.append(idx)
        print(maxArea)
        return maxArea



Solution().largestRectangleArea([1,2,3,4,5])