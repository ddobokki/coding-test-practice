from typing import List


class Solution(object):
    def exist(self, board, word):
        def checkWord(index, i, j):
            if index == len(word): # 끝까지 탐색이 완료되면 True 리턴
                return True
            steps = [(0, 1), (1, 0), (-1, 0), (0, -1)] # 다음 오른쪽 왼쪽 위, 아래
            for x1, y1 in steps:
                x_new = x1 + i # 다음 좌표 4번 반복
                y_new = y1 + j

                if 0 <= x_new < m and 0 <= y_new < n: # 보드의 밖을 나가지 않고
                    if not visited[x_new][y_new] and board[x_new][y_new] == word[index]: # 방문하지 않고, 다음 단어면
                        visited[x_new][y_new] = True # 방문 표시
                        if checkWord(index + 1, x_new, y_new): # 다음 글자 탐색
                            return True

            visited[i][j] = False # board[i][j]에서 탐색이 끝나지 않았으면 다음을 선택해서 가야 하기 때문에 다시 False로

            return False

        m = len(board)
        n = len(board[0])
        s = len(word)
        if (m == 0 and n == 0) or (s == 0):
            return False

        visited = [[False] * n for j in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if checkWord(1, i, j):
                        return True
                    visited[i][j] = False

        return False


Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED")
