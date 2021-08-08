'''
P   A   H   N
A P L S I I G
Y   I   R

'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s
        temp = [['']*len(s) for i in range(numRows)]

        temp[0][0] = s[0]
        cnt = len(s) - 1
        idx = 1
        y, x = 0, 0
        state = 1
        while cnt > 0:

            if state == 1:
                for i in range(numRows - 1):
                    if cnt == 0:
                        break
                    y += 1
                    temp[y][x] = s[idx]
                    idx += 1
                    cnt -= 1

                state = 0

            if state == 0:
                for i in range(numRows - 1):
                    if cnt == 0:
                        break
                    y -= 1
                    x += 1
                    temp[y][x] = s[idx]
                    idx += 1
                    cnt -= 1
                state = 1

        ans = ""
        for t in temp:
            ans += ''.join(t)

        return ans

#print(Solution().convert("PAYPALISHIRING",3))
print(Solution().convert("ab",1))
# sss = "PAYPALISHIRING"
# print(sss[13])