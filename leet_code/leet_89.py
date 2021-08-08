from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:

        return([i^(i>>1) for i in range(2**n)])
'''
000
001
011
010
110
111
101
100
'''

print(Solution().grayCode(2))
print(1>>1)