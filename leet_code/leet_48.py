from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rotation_matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        N = len(matrix)
        for x in range(N):
            for y in range(N):
                rotation_matrix[y][x] = matrix[N - x - 1][y]

        for x in range(N):
            for y in range(N):
                matrix[y][x] = rotation_matrix[y][x]
