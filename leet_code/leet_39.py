from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = set()

        def dfs(cur,li):
            li.append(cur)
            sum_li = sum(li)

            if sum_li == target:
                li.sort()
                result.add(tuple(li))
                return

            if sum_li > target:
                return

            for i in range(len(candidates)):
                temp = li.copy()
                dfs(candidates[i],temp)

        for k in range(len(candidates)):
            temp = []
            dfs(candidates[k],temp)

        return list(result)



print(Solution().combinationSum([2,3,5],8))

