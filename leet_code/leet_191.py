class Solution:
    def hammingWeight(self, n: int) -> int:
        b = "{0:032b}".format(n)
        return b.count('1')