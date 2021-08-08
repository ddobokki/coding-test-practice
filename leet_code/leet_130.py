from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visit = [[False] * n for _ in range(m)]
        def dfs(board,y,x):
            dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            # up, down, left, right
            #print(x,y)
            if not visit[y][x]:
                board[y][x] = 'T'
                visit[y][x] = True
            else:
                return

            for dx,dy in dirs:
                nx = x + dx
                ny = y + dy
                if (1 <= nx < n - 1 and 1 <= ny < m - 1) and board[ny][nx] == 'O':
                    if not visit[ny][nx]:

                        dfs(board,ny,nx)
            return

        # find 'O' in outlying

        for i in range(m):
            for j in range(n):
                if not (1 <= j < n - 1 and 1 <= i < m - 1) and board[i][j] == 'O':
                    print(i,j)
                    dfs(board, i, j)
                else:
                    continue

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'



board = [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]

Solution().solve(board)

'''
모범 코드
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # do search on border values and mark grouped number islands to border
        # set all unmarked to x 
        # not thread safe
        
        for row in range(len(board)):
            
            if board[row][0] == "O":
                self.dfs(board, row, 0)
            if board[row][-1] == "O":
                self.dfs(board, row, len(board[0])-1)
        
        for col in range(len(board[0])):
            
            if board[0][col] == "O":
                self.dfs(board, 0, col)
            if board[-1][col] == "O":
                self.dfs(board, len(board)-1, col)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '#':
                    board[row][col] = 'O'
                else:
                    board[row][col] = 'X'
        
    
    def dfs(self, board, row, col):
        
        checks = ((0,1), (0,-1), (1,0), (-1,0))
        board[row][col] = '#'
        
        for r, c in checks:
            newr = row+r
            newc = col+c
            
            if newr >= 0 and newr < len(board) and newc >= 0 and newc < len(board[0]):
                if board[newr][newc] == 'O':
                    self.dfs(board, newr, newc)
        

'''