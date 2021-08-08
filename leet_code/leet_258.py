class Solution:
    def addDigits(self, num: int) -> int:
        string_num = str(num)

        while len(string_num) != 1:
            temp = 0

            for digit in string_num:
                temp += int(digit)
            string_num = str(temp)

        return int(string_num)