from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        output = [[]]

        idx = 0

        while idx < len(nums):
            cur = nums[idx]
            for i in range(idx, len(nums)):
                if i == idx:
                    output.append(output[0] + [nums[i]])
                else:
                    output.append(output[-1] + [nums[i]])
            idx += 1
        output = list(set(list(map(lambda x: tuple(x), output))))
        output = list(map(lambda x: list(x), output))
        output.sort()
        #print(output)
        return output

Solution().subsetsWithDup([1,2,2])
Solution().subsetsWithDup([0])