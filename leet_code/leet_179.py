from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str,nums))
        nums = sorted(nums,key=lambda x: x*10,reverse=True)

        return str(int(''.join(nums)))

Solution().largestNumber([10,2])
Solution().largestNumber([3,30,34,5,9])