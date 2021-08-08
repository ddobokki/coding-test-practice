class Solution:
    def isUgly(self, n: int) -> bool:

        ugly_primes = [2,3,5]

        if n <= 0:
            return False

        while n > 1:

            for ugly_prime in ugly_primes:
                if n % ugly_prime == 0:
                    n = n // ugly_prime
                    break
            else:
                return False

        return True

print(Solution().isUgly(6))