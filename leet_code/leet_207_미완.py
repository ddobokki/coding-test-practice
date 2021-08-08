from typing import List

import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        coures = collections.defaultdict(list)

        for after, before in prerequisites:
            coures[after].append(before)
        path = set()
        visit = set()

        def dfs(i):

            if i in path:
                return False

            if i in visit:
                return True

            path.add(i)

            for j in coures[i]:
                if not dfs(j):
                    return False
            path.remove(i)
            visit.add(i)

            return True

        for i in list(coures):
            if not dfs(i):
                return False
        return True


print(Solution().canFinish(5,[[1,4],[2,4],[3,1],[3,2]]))
