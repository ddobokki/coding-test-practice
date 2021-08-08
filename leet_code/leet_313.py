from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        uglys = [1]

        pointers = [0]*len(primes)

        while len(uglys) != n:
            next = []
            for i in range(len(pointers)):
                next.append(uglys[pointers[i]]*primes[i])
            next_ugly = min(next)
            uglys.append(next_ugly)

            for i in range(len(pointers)):
                if next_ugly == next[i]:
                    pointers[i] += 1
        #print(uglys)
        return uglys[-1]
Solution().nthSuperUglyNumber(12,[2,7,13,19])