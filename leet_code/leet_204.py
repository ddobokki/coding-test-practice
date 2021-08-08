class Solution:
    def countPrimes(self, n: int) -> int:
        cnt, sieve = 0, [True] * n #
        for i in range(2, n):
            if sieve[i]:
                cnt = cnt + 1
                for i in range(i * i, n, i):
                    sieve[i] = False
        return cnt

Solution().countPrimes(10)

#print(solution(4))