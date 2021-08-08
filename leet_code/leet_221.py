from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_width = -1

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != '0':
                    matrix[i][j] = min(int(matrix[i - 1][j]), int(matrix[i][j - 1]),int(matrix[i - 1][j - 1])) + 1
                    max_width = max(max_width, matrix[i][j])

        if max_width == -1:
            for m in matrix:
                for n in m:
                    max_width = max(max_width,int(n))

            return max_width** 2

        for m in matrix:
            print(m)

        return max_width ** 2

Solution().maximalSquare([["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]])