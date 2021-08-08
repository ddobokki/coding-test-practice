class Solution:
    str_digit = [chr(i) for i in range(ord('A'),ord('Z') + 1)]


    def convert(self,nums, base):
        nums -= 1
        q, r = divmod(nums, base)
        if q == 0:
            return self.str_digit[r]
        else:
            return self.convert(q, base) + self.str_digit[r]


    def convertToTitle(self, columnNumber: int) -> str:


        return self.convert(columnNumber,26)

Solution().convertToTitle(701)