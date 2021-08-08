from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == 0:
                    y_idx = y
                    x_idx = x + 1
                    while x_idx < len(matrix[0]):
                        if matrix[y][x_idx] == 0:
                            break
                        matrix[y][x_idx] = 'c'
                        x_idx += 1
                    x_idx = x - 1
                    while x_idx >= 0:
                        if matrix[y][x_idx] == 0:
                            break
                        matrix[y][x_idx] = 'c'
                        x_idx -= 1
                    y_idx = y + 1
                    x_idx = x
                    while y_idx < len(matrix):
                        if matrix[y_idx][x] == 0:
                            break
                        matrix[y_idx][x] = 'c'
                        y_idx += 1
                    y_idx = y - 1
                    while y_idx >= 0:
                        if matrix[y_idx][x] == 0:
                            break
                        matrix[y_idx][x] = 'c'
                        y_idx -= 1
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == 'c':
                    matrix[y][x] = 0


Solution().setZeroes(matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]])
