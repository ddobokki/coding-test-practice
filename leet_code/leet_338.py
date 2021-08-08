from typing import List


class Solution:
    def bit_count(self,n):
        cnt = 0
        while n > 0:
            n &= n - 1
            cnt += 1
        return cnt

    def countBits(self, num: int) -> List[int]:

        nums = list(range(0,num+1))

        for i in range(len(nums)):
            nums[i] = self.bit_count(nums[i])
        return nums
Solution().countBits(5)

