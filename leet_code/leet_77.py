from typing import List

import itertools
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        return list(itertools.combinations(list(range(1,n+1)),k))

print(Solution().combine(4,2))