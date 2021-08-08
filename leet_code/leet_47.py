from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = set()
        def dfs(num,li,candidate):

            li.append(num)
            candidate.remove(num)
            if len(li) == len(nums):
                result.add(tuple(li))
                return

            for n in candidate:
                dfs(n,li[:],candidate[:])

        for num in nums:
            dfs(num,[],nums[:])


        return list(result)