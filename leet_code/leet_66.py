from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digits[-1] += 1

        right = len(digits) - 1

        while right > 0:

            if digits[right] == 10:
                digits[right] = 0
                digits[right - 1] += 1
            right -= 1

        if digits[0] == 10:
            digits[0] = 0
            digits = [1] + digits

        return digits
Solution().plusOne([9,9,9])