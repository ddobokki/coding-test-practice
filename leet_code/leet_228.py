from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        range_list = []
        if len(nums) == 0:
            return []
        pointer = 1
        stack = [nums[0]]
        while pointer < len(nums):
            if nums[pointer] == stack[-1]+1:
                stack.append(nums[pointer])
            else:
                if len(stack) == 1:
                    range_list.append(str(stack[-1]))
                else:
                    range_list.append(str(stack[0]) + "->"+str(stack[-1]))
                stack.clear()
                stack.append(nums[pointer])
            pointer += 1
        if len(stack) == 1:
            range_list.append(str(stack[-1]))
        else:
            range_list.append(str(stack[0]) + "->" + str(stack[-1]))

        return range_list

Solution().summaryRanges([0,1,2,4,5,7])
Solution().summaryRanges([0,2,3,4,6,8,9])