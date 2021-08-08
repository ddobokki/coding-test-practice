from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        state = 0
        y, x = 0,0
        ans = []
        n, m = len(matrix), len(matrix[0])

        while True:
            #print(state)
            if state == 0:
                for i in range(x,m):
                    e = matrix[y][i]
                    x = i
                    if e != -200:
                        ans.append(e)
                        matrix[y][i] = -200
                    else:
                        x -= 1
                        break

                state = 1
            print(x)
            if state == 1:
                for i in range(y+1, n):
                    e = matrix[i][x]
                    y = i
                    if e != - 200:
                        ans.append(matrix[i][x])
                        matrix[i][x] = -200
                    else:
                        y -= 1
                        break
                state = 2
            #print(x)
            if state == 2:
                for i in range(x - 1, -1, -1):
                    e = matrix[y][i]
                    x = i
                    if e != - 200:

                        ans.append(matrix[y][i])
                        matrix[y][i] = -200
                    else:
                        x += 1
                        break
                state = 3

            if state == 3:
                for i in range(y - 1, -1, - 1):
                    e = matrix[i][x]
                    y = i
                    if e != -200:
                        ans.append(matrix[i][x])
                        matrix[i][x] = - 200
                    else:
                        y += 1
                        break
                x += 1
                state = 0
            if len(ans) == m*n:
                break
        return ans

Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])