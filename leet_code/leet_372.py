from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if a in [1,0]:
            return a
        return int(pow(a,int("".join(str(i) for i in b)),1337))


