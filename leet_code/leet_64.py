from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        for y in range(1,len(grid)):
            grid[y][0] += grid[y - 1][0]

        for x in range(1,len(grid[0])):
            grid[0][x] += grid[0][x - 1]

        for y in range(1,len(grid)):
            for x in range(1,len(grid[0])):
                up = grid[y - 1][x]
                left = grid[y][x - 1]
                grid[y][x] = min(grid[y][x] + up, grid[y][x] + left)


        return grid[-1][-1]

Solution().minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]])