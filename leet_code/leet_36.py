from typing import List




class Solution:

    def check_33box(self, board: List[List[str]]):
        for k in range(3):
            temp1 = []
            temp2 = []
            temp3 = []
            for i in range(3):

                for j in range(9):
                    n = board[3 * k + i][j]
                    if n.isdigit():
                        if 0 <= j <= 2:
                            temp1.append(n)
                        if 3 <= j <= 5:
                            temp2.append(n)
                        if 6 <= j <= 8:
                            temp3.append(n)
            if len(temp1) != len(set(temp1)) or len(temp2) != len(set(temp2)) or len(temp3) != len(set(temp3)):
                return False
        return True

    def check_diagonal(self, board: List[List[str]]):

        for i in range(len(board)):
            temp = []
            for j in range(len(board[i])):
                n = board[i][j]
                if n.isdigit():
                    temp.append(n)
            if len(temp) != len(set(temp)):
                return False
        return True

    def check_length(self,board: List[List[str]]):

        for i in range(len(board[0])):
            temp = []
            for j in range(len(board)):
                n = board[j][i]
                if n.isdigit():
                    temp.append(n)

            if len(temp) != len(set(temp)):
                return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        if not self.check_33box(board):
            return False
        if not self.check_diagonal(board):
            return False
        if not self.check_length(board):
            return False

        return True


print(Solution().check_33box([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
