from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if obstacleGrid[-1][-1] == 1:
            return 0

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1

        for i in range(len(obstacleGrid[0])):
            if (obstacleGrid[0][i] != -1):
                obstacleGrid[0][i] = 1
            else:
                break

        for j in range(len(obstacleGrid)):
            if (obstacleGrid[j][0] != -1):
                obstacleGrid[j][0] = 1
            else:
                break

        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[i])):
                if (obstacleGrid[i][j] == -1):
                    continue
                up = obstacleGrid[i - 1][j]
                left = obstacleGrid[i][j - 1]

                if (up != -1 and left != -1):
                    obstacleGrid[i][j] = up + left
                elif (up == -1 and left != -1):
                    obstacleGrid[i][j] = left
                elif (left == -1 and up != -1):
                    obstacleGrid[i][j] = up
                else:
                    obstacleGrid[i][j] = -1
        if obstacleGrid[-1][-1] == -1:
            return 0

        return obstacleGrid[-1][-1]