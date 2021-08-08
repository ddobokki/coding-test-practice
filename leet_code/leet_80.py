from typing import List

import collections
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_count = collections.Counter(nums)
        before_len = len(nums)
        cur_idx = 0
        for n in nums_count:
            if nums_count[n] >= 2:
                for i in range(2):
                    nums[cur_idx] = n
                    cur_idx += 1
            else:
                nums[cur_idx] = n
                cur_idx += 1

        for _ in range(before_len - cur_idx):
            nums.pop()

        return len(nums)

'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for num in nums:
            while nums.count(num) > 2:
                nums.remove(num)
         return len(nums)
         
간단하게 푸는 방법이지만 remove 때문에 시간이 좀 걸릴것 같다?
'''


Solution().removeDuplicates([1,1,1,2,2,3])
Solution().removeDuplicates([0,0,1,1,1,1,2,3,3])