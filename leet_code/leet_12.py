'''
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

'''
import math


class Solution:
    def intToRoman(self, num: int) -> str:
        split_by = []
        len_n = int(math.log10(num))
        divide = 10 ** len_n
        while divide > 0:
            split_by.append((num // divide) * divide)
            num = num % divide
            divide = divide // 10

        roman_num_dict = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M',
                          4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}

        rndk = sorted(roman_num_dict.keys())
        ans = ''
        for n in split_by:
            if n in roman_num_dict:
                ans += roman_num_dict[n]
            else:
                while n != 0:
                    idx = 0
                    for i, dk in enumerate(rndk):
                        idx = i
                        if n - dk < 0:
                            idx = i - 1
                            break

                    ans += roman_num_dict[rndk[idx]]
                    n -= rndk[idx]
        return ans
temp_dict = {}
for i in range(1,4000):
    temp_dict[Solution().intToRoman(i)] = i
print(temp_dict)
