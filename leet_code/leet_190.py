class Solution:
    def reverseBits(self, n: int) -> int:
        b = "{0:032b}".format(n)
        return int(b[::-1],2)
