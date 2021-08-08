from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = set()

        def dfs(idx, candi, li):
            li.append(candi.pop(idx))
            sum_li = sum(li)
            if sum_li == target:
                li.sort()
                result.add(tuple(li))
                return

            if sum_li > target:
                return

            for i in range(len(candi)):
                dfs(i, candi[:], li[:])

        if sum(candidates) == target:
            return [candidates]
        if sum(candidates) < target:
            return [[]]
        for k in range(len(candidates)):
            dfs(k, candidates[:], [])

        return list(result)


print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(sum([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))