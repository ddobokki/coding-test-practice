from typing import List

import itertools
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1,10))
        choice = list(itertools.combinations(nums,k))
        #print(choice)
        a = []
        for c in choice:
            s = 0
            for i in c:
                s += i
                if s > n:
                    break
            if s == n:
                a.append(list(c))
        return a

print(Solution().combinationSum3(3,7))