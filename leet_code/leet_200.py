from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        def dfs(grid,y,x):
            dirs = [(0,1),(0,-1),(1,0),(-1,0)]

            if grid[y][x] == '0':
                return

            grid[y][x] = '0'

            # left, right, down, up
            for dy,dx in dirs:
                nx = x + dx
                ny = y + dy
                if 0<= ny < len(grid) and 0 <= nx < len(grid[0]):
                    dfs(grid,ny,nx)


        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    dfs(grid,i,j)
                    cnt += 1
        #print(cnt)
        return cnt

Solution().numIslands( [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])