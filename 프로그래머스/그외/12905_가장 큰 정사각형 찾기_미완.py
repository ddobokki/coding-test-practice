# https://programmers.co.kr/learn/courses/30/lessons/12905
def solution(board):
    max_l = 0
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[i][j] != 0:
                board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1
                if(board[i][j] > max_l):
                    max_l = board[i][j]
    if max_l == 0 and board[0][0] == 1
        max_l = 1
    return max_l*max_l


a = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]

for aa in a:
    print(aa)

print("")
solution(a)
