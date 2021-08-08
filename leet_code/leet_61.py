class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = [[0]*n for _ in range(m)]

        for i in range(m):
            path[i][0] = 1

        for i in range(n):
            path[0][i] = 1

        for y in range(1, m):
            for x in range(1, n):
                path[y][x] = path[y - 1][x] + path[y][x - 1]

        return path[-1][-1]


Solution().uniquePaths(1,1)