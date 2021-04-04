def check(x, y, n, board_x):
    for i in range(x):
        if y == board_x[i] or abs(y - board_x[i]) == x - i:
            return False
    return True


def queen(x, n, board_x):
    if x == n:
        return 1

    count = 0

    for y in range(n):
        if check(x, y, n, board_x):
            board_x[x] = y
            count += queen(x + 1, n, board_x)

    return count


def solution(n):
    board_x = [0] * n
    answer = queen(0, n, board_x)

    return answer


# import itertools
# def check(board, points_list):
#     for p in points_list:
#         y, x = p
#
#         # 수평
#         for i in range(1, len(board)):
#             if x + i < len(board):
#                 if board[y][x + i] == 1:
#                     return False
#             else:
#                 break
#         for i in range(1, len(board)):
#             if x - i >= 0:
#                 if board[y][x - i] == 1:
#                     return False
#             else:
#                 break
#         # 수직
#         for i in range(1, len(board)):
#             if y + i < len(board):
#                 if board[y + i][x] == 1:
#                     return False
#             else:
#                 break
#         for i in range(1, len(board)):
#             if y - i >= 0:
#                 if board[y - i][x] == 1:
#                     return False
#             else:
#                 break
#         # 대각선 9 3 1 7
#         for i in range(1, len(board)):
#             if x + i < len(board) and y - i >= 0:
#                 if board[y - i][x + i] == 1:
#                     return False
#             else:
#                 break
#         for i in range(1, len(board)):
#             if x + i < len(board) and y + i < len(board):
#                 if board[y + i][x + i] == 1:
#                     return False
#             else:
#                 break
#         for i in range(1, len(board)):
#             if x - i >= 0 and y + i < len(board):
#                 if board[y + i][x - i] == 1:
#                     return False
#             else:
#                 break
#         for i in range(1, len(board)):
#             if x - i >= 0 and y - i >= 0:
#                 if board[y - i][x - i] == 1:
#                     return False
#             else:
#                 break
#
#     return True
#
#
# def solution(n):
#     answer = 0
#
#     points = list(itertools.combinations(range(n*n), n))
#     cnt = 0
#     for point in points:
#         board = [[0] * n for _ in range(n)]
#         yx = []
#         for p in point:
#             board[p // n][p % n] = 1
#             yx.append([p // n, p % n])
#         if check(board, yx):
#             # for b in board:
#             #     print(b)
#             print(yx)
#             cnt += 1
#     return cnt

#
# print(1,solution(1))
# print(2,solution(2))
# print(3,solution(3))
print(4, solution(4))
print(5, solution(5))
print(6, solution(6))

'''
1 1
2 0
3 0
4 2
5 10
6 4


[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
4 2
[[0, 0], [1, 2], [2, 4], [3, 1], [4, 3]]
[[0, 0], [1, 3], [2, 1], [3, 4], [4, 2]]
[[0, 1], [1, 3], [2, 0], [3, 2], [4, 4]]
[[0, 1], [1, 4], [2, 2], [3, 0], [4, 3]]
[[0, 2], [1, 0], [2, 3], [3, 1], [4, 4]]
[[0, 2], [1, 4], [2, 1], [3, 3], [4, 0]]
[[0, 3], [1, 0], [2, 2], [3, 4], [4, 1]]
[[0, 3], [1, 1], [2, 4], [3, 2], [4, 0]]
[[0, 4], [1, 1], [2, 3], [3, 0], [4, 2]]
[[0, 4], [1, 2], [2, 0], [3, 3], [4, 1]]
5 10
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
6 4
'''
