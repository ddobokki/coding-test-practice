def guess(n):
    pass

class Solution:
    def guessNumber(self, n: int) -> int:

        left = 1
        right = n

        while left <= right:
            mid = left + (right - left) // 2
            condi = guess(mid)
            if condi == 0:
                return mid
            elif condi == 1:
                left = mid + 1
            else:
                right = mid - 1


print((1+2) // 2)