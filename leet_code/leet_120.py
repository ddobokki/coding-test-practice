from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # if len(triangle) == 1:
        #     return triangle[-1][-1]

        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] = triangle[i][j] + triangle[i - 1][j]
                    continue
                if j == len(triangle[i]) - 1:
                    triangle[i][j] = triangle[i][j] + triangle[i - 1][j-1]
                    continue

                triangle[i][j] = min(triangle[i][j] + triangle[i-1][j - 1],triangle[i][j] + triangle[i-1][j])

        return min(triangle[-1])
Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
Solution().minimumTotal([[2],[3,4]])

'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[-1][-1]

        tri = [triangle[0]]
        for i in range(1,len(triangle)):
            temp = []
            for j in range(len(triangle[i])):
                if j == 0:
                    temp.append(triangle[i][j] + tri[i - 1][j])
                    continue
                if j == len(triangle[i]) - 1:
                    temp.append(triangle[i][j] + tri[i - 1][j - 1])
                    continue

                temp.append(min(triangle[i][j] + tri[i-1][j - 1],triangle[i][j] + tri[i-1][j]))
            tri.append(temp)
        print(tri)

'''