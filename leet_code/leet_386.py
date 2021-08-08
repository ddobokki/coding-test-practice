from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = list(range(1,n+1))
        ans.sort(key=lambda x:str(x))

        return ans

Solution().lexicalOrder(13)