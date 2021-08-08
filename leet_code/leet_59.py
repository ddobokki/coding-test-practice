from typing import List

import collections
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        num = collections.deque(list(range(1,n*n + 1)))

        state = 0
        y, x = 0, 0
        matrix = [[-200]*n for i in range(n)]


        while True:
            if state == 0:
                for i in range(x, n):
                    #print(matrix)
                    e = matrix[y][i]
                    x = i
                    if e == -200:
                        matrix[y][i] = num.popleft()
                    else:
                        x -= 1
                        break

                state = 1

            if state == 1:
                for i in range(y + 1, n):
                    #print(matrix)
                    e = matrix[i][x]
                    y = i
                    if e == -200:
                        matrix[i][x] = num.popleft()
                    else:
                        y -= 1
                        break
                state = 2
            #print(y)
            if state == 2:
                for i in range(x - 1, -1, -1):
                    #print(matrix)
                    e = matrix[y][i]
                    x = i
                    if e == -200:
                        matrix[y][i] = num.popleft()
                    else:
                        x += 1
                        break
                state = 3

            if state == 3:
                #print(matrix)
                for i in range(y - 1, -1, - 1):
                    e = matrix[i][x]
                    y = i
                    if e == -200:
                        matrix[i][x] = num.popleft()
                    else:
                        y += 1
                        break
                x += 1
                state = 0
            if not num:
                break
        return matrix

print(Solution().generateMatrix(3))



