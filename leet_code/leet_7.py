class Solution:
    def reverse(self, x: int) -> int:
        str_x = list(str(abs(x)))

        if x > 0:
            x = int(''.join(str_x[::-1]))
        else:
            x = -1 * int(''.join(str_x[::-1]))

        if not -2**31 <=x <= 2**31 -1:
            return 0
        else:
            return x

