from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        prediff = nums[1] - nums[0]

        if prediff != 0:
            count = 2
        else:
            count = 1

        for i in range(2,len(nums)):
            diff = nums[i] - nums[i-1]

            if diff > 0 and prediff <= 0 or diff < 0 and prediff >= 0:
                count += 1
                prediff = diff
        #print(count)
        return count

Solution().wiggleMaxLength([1,7,4,9,2,5])
Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])
Solution().wiggleMaxLength([1,2,3,4,5,6,7,8,9])