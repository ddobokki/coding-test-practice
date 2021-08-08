from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        idx = 0
        curr = nums[idx]
        count = 0
        result = []
        while idx < len(nums):
            if nums[idx] == curr:
                count += 1
            else:
                if count == 1:
                    result.append(curr)

                curr = nums[idx]
                count = 1
            idx += 1
        if count == 1: # 마지막이 하나 있을 경우
            result.append(curr)
        return result
        #print(result)
Solution().singleNumber([1,2])